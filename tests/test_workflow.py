import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from abm_engine.library import SignalLibrary
from abm_engine.workflow import build_message_brief, run_account, score_evidence_payload, validate_evidence


ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = SignalLibrary.from_json(ROOT / "data" / "industry-agnostic-signals.json")

    def test_sparse_crm_input_fails_closed_without_message_brief(self):
        with TemporaryDirectory() as directory:
            out = Path(directory) / "attio"
            result = run_account(
                library=self.library,
                brief={},
                company_name="Attio",
                domain="attio.com",
                industry="B2B SaaS CRM",
                output_dir=out,
            )
            self.assertEqual("needs_input", result.status)
            self.assertIn("offer", result.missing)
            self.assertTrue((out / "account-manifest.json").exists())
            self.assertFalse((out / "message-brief.md").exists())
            manifest = json.loads((out / "account-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual("industry-agnostic-v1", manifest["signal_pack"])

    def test_complete_brief_moves_only_to_research(self):
        brief = {
            "seller_identity": "Named seller",
            "offer": "Documented offer",
            "buyer_role": "VP Marketing",
            "campaign_objective": "Validate fit",
            "desired_action": "Review one workflow",
            "operating_problem": "A source-backed operating problem.",
            "consequence": "A bounded consequence to validate.",
            "proof_points": ["Approved proof"],
        }
        with TemporaryDirectory() as directory:
            result = run_account(
                library=self.library,
                brief=brief,
                company_name="Attio",
                domain="attio.com",
                industry="B2B SaaS CRM",
                output_dir=Path(directory),
            )
        self.assertEqual("needs_research", result.status)

    def test_evidence_requires_https_dates_rationale_reviewer_and_approval(self):
        payload = {"items": [{"signal_key": "public_product_launch", "source_url": "http://x", "confidence": 2}]}
        errors = validate_evidence(payload, self.library)
        self.assertTrue(any("valid HTTPS" in error for error in errors))
        self.assertTrue(any("approval_status" in error for error in errors))
        self.assertTrue(any("confidence must be between" in error for error in errors))

    def test_only_approved_evidence_scores(self):
        base = {
            "signal_key": "public_product_launch",
            "observation": "Company announced a dated product launch.",
            "source_url": "https://example.com/launch",
            "source_date": "2026-08-01",
            "accessed_at": "2026-08-07",
            "confidence": 0.8,
            "confidence_rationale": "First-party announcement.",
            "reviewer": "Reviewer",
        }
        payload = {"account": "Example", "items": [{**base, "approval_status": "pending"}, {**base, "approval_status": "approved"}]}
        result = score_evidence_payload(payload, self.library)
        self.assertEqual(0.6, result["score"])
        self.assertFalse(result["contributions"][0]["approved"])

    def test_message_brief_requires_approved_evidence_and_complete_campaign(self):
        campaign = {
            "seller_identity": "Named seller",
            "offer": "Documented offer",
            "buyer_role": "VP Marketing",
            "campaign_objective": "Validate fit",
            "desired_action": "Review one workflow",
            "operating_problem": "A source-backed operating problem.",
            "consequence": "A bounded consequence to validate.",
            "proof_points": ["Approved proof"],
            "prohibited_claims": ["Do not claim purchase intent."],
        }
        evidence = {
            "account": "Attio",
            "items": [{
                "signal_key": "public_product_launch",
                "observation": "Attio announced a dated product launch.",
                "source_url": "https://example.com/launch",
                "source_date": "2026-08-01",
                "accessed_at": "2026-08-07",
                "confidence": 0.8,
                "confidence_rationale": "First-party announcement.",
                "reviewer": "Reviewer",
                "approval_status": "approved",
            }],
        }
        rendered = build_message_brief(brief=campaign, evidence=evidence, library=self.library)
        self.assertIn("Attio announced a dated product launch.", rendered)
        self.assertIn("Do not claim adoption", rendered)
        pending = {**evidence, "items": [{**evidence["items"][0], "approval_status": "pending"}]}
        with self.assertRaisesRegex(ValueError, "approved evidence"):
            build_message_brief(brief=campaign, evidence=pending, library=self.library)


if __name__ == "__main__":
    unittest.main()
