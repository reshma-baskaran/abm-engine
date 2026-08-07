from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from .library import SignalLibrary


REQUIRED_BRIEF_FIELDS = (
    "seller_identity",
    "offer",
    "buyer_role",
    "campaign_objective",
    "desired_action",
    "operating_problem",
    "consequence",
    "proof_points",
)
APPROVAL_STATES = {"pending", "approved", "rejected"}


@dataclass(frozen=True)
class WorkflowResult:
    status: str
    missing: tuple[str, ...]
    output_dir: Path
    recommended_signals: int

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "missing": list(self.missing),
            "output_dir": str(self.output_dir),
            "recommended_signals": self.recommended_signals,
            "message_brief_created": False,
        }


def load_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return payload


def missing_brief_fields(brief: dict) -> list[str]:
    missing: list[str] = []
    for field in REQUIRED_BRIEF_FIELDS:
        value = brief.get(field)
        if isinstance(value, str) and value.strip():
            continue
        if isinstance(value, list) and any(str(item).strip() for item in value):
            continue
        missing.append(field)
    return missing


def _render_research_record(company_name: str, domain: str, industry: str, status: str, signals: list[dict]) -> str:
    lines = [
        "---",
        "type: account-research",
        f'account: "{company_name}"',
        f'domain: "{domain}"',
        f'industry: "{industry}"',
        f'research_date: "{date.today().isoformat()}"',
        f'workflow_status: "{status}"',
        'relationship_claim: "none unless verified"',
        "---",
        "",
        f"# Account research record — {company_name}",
        "",
        "## Recommended research hypotheses",
        "",
        "| Signal key | Why it is portable | Research query |",
        "|---|---|---|",
    ]
    for signal in signals:
        query = str(signal["query"]).replace("|", "\\|")
        applicability = str(signal["applicability"]).replace("|", "\\|")
        lines.append(f"| `{signal['signal_key']}` | {applicability} | `{query}` |")
    lines.extend(
        [
            "",
            "## Evidence",
            "",
            "No account claim is approved yet. Add evidence to `evidence.json`, then run `evidence-validate`.",
            "",
            "## Unknowns and suppressions",
            "",
            "- A signal definition is not proof that the signal exists at this account.",
            "- Public evidence does not prove budget, urgency, dissatisfaction, or purchase intent.",
            "- Do not use a signal whose applicability or freshness requirements are not met.",
            "",
        ]
    )
    return "\n".join(lines)


def run_account(
    *,
    library: SignalLibrary,
    brief: dict,
    company_name: str,
    domain: str,
    industry: str,
    output_dir: Path,
    limit: int = 8,
) -> WorkflowResult:
    output_dir.mkdir(parents=True, exist_ok=True)
    missing = missing_brief_fields(brief)
    status = "needs_input" if missing else "needs_research"
    ranked = sorted(
        library.signals,
        key=lambda signal: (signal.confidence or 0.0, signal.weight or 0.0),
        reverse=True,
    )[:limit]
    recommendations = [
        {
            "signal_key": signal.key,
            "category": signal.category,
            "applicability": signal.applicability,
            "disqualifiers": list(signal.disqualifiers),
            "source_priority": list(signal.source_priority),
            "freshness_days": signal.freshness_days,
            "safe_interpretation": signal.safe_interpretation,
            "prohibited_inference": signal.prohibited_inference,
            "query": signal.render_query(company_name=company_name, company_domain=domain, ticker=""),
        }
        for signal in ranked
    ]
    manifest = {
        "account": company_name,
        "domain": domain,
        "industry": industry,
        "signal_pack": ranked[0].pack if ranked else "unknown",
        "status": status,
        "missing": missing,
        "recommended_signals": recommendations,
        "next_command": "Complete the missing campaign fields." if missing else "Add source-backed observations to evidence.json.",
    }
    (output_dir / "account-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (output_dir / "campaign-brief.json").write_text(json.dumps(brief, indent=2) + "\n", encoding="utf-8")
    (output_dir / "research-record.md").write_text(
        _render_research_record(company_name, domain, industry, status, recommendations), encoding="utf-8"
    )
    evidence = {
        "account": company_name,
        "research_date": date.today().isoformat(),
        "signal_pack": manifest["signal_pack"],
        "items": [],
    }
    (output_dir / "evidence.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    return WorkflowResult(status, tuple(missing), output_dir, len(recommendations))


def _valid_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_evidence(payload: dict, library: SignalLibrary) -> list[str]:
    errors: list[str] = []
    items = payload.get("items")
    if not isinstance(items, list) or not items:
        return ["Evidence record must contain at least one item."]
    known = {signal.key: signal for signal in library.signals}
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            errors.append(f"Item {index} must be an object.")
            continue
        key = str(item.get("signal_key", "")).strip()
        if key not in known:
            errors.append(f"Item {index} uses a signal outside the selected pack: {key or '<blank>'}.")
        for field in ("observation", "source_date", "accessed_at", "confidence_rationale", "reviewer"):
            if not str(item.get(field, "")).strip():
                errors.append(f"Item {index} is missing {field}.")
        if not _valid_https_url(item.get("source_url")):
            errors.append(f"Item {index} must contain a valid HTTPS source_url.")
        confidence = item.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= float(confidence) <= 1:
            errors.append(f"Item {index} confidence must be between 0 and 1.")
        approval = str(item.get("approval_status", "")).strip()
        if approval not in APPROVAL_STATES:
            errors.append(f"Item {index} approval_status must be pending, approved, or rejected.")
    return sorted(set(errors))


def score_evidence_payload(payload: dict, library: SignalLibrary) -> dict:
    errors = validate_evidence(payload, library)
    if errors:
        raise ValueError("\n".join(errors))
    known = {signal.key: signal for signal in library.signals}
    contributions = []
    for item in payload["items"]:
        signal = known[item["signal_key"]]
        approved = item["approval_status"] == "approved"
        score = round((signal.weight or 0.0) * float(item["confidence"]), 3) if approved else 0.0
        contributions.append({"signal_key": signal.key, "approved": approved, "score": score})
    return {
        "account": payload.get("account", ""),
        "score": round(sum(item["score"] for item in contributions), 3),
        "contributions": contributions,
        "warning": "This is an evidence-prioritization score, not probability of purchase or buying intent.",
    }


def build_message_brief(*, brief: dict, evidence: dict, library: SignalLibrary) -> str:
    missing = missing_brief_fields(brief)
    if missing:
        raise ValueError(f"campaign brief is missing: {', '.join(missing)}")
    errors = validate_evidence(evidence, library)
    if errors:
        raise ValueError("\n".join(errors))
    approved = [item for item in evidence["items"] if item["approval_status"] == "approved"]
    if not approved:
        raise ValueError("message brief requires at least one approved evidence item")
    known = {signal.key: signal for signal in library.signals}
    lines = [
        "---",
        "type: message-brief",
        f'account: "{evidence.get("account", "")}"',
        'review_status: "draft_requires_human_review"',
        "---",
        "",
        f"# Message brief — {evidence.get('account', '')}",
        "",
        "## Campaign context",
        "",
        f"- Seller: {brief['seller_identity']}",
        f"- Offer: {brief['offer']}",
        f"- Buyer role: {brief['buyer_role']}",
        f"- Objective: {brief['campaign_objective']}",
        "",
        "## Operating problem",
        "",
        str(brief["operating_problem"]),
        "",
        "## Consequence",
        "",
        str(brief["consequence"]),
        "",
        "## Approved evidence that can be stated",
        "",
        "| Claim | Source URL | Confidence | Reviewer |",
        "|---|---|---|---|",
    ]
    for item in approved:
        observation = str(item["observation"]).replace("|", "\\|")
        lines.append(f"| {observation} | {item['source_url']} | {item['confidence']} | {item['reviewer']} |")
    lines.extend(["", "## Evidence boundaries", ""])
    for item in approved:
        signal = known[item["signal_key"]]
        lines.append(f"- `{signal.key}`: {signal.prohibited_inference}")
    for claim in brief.get("prohibited_claims", []):
        if str(claim).strip():
            lines.append(f"- {claim}")
    lines.extend([
        "",
        "## Approved proof points",
        "",
        *[f"- {proof}" for proof in brief["proof_points"]],
        "",
        "## Suggested next step",
        "",
        str(brief["desired_action"]),
        "",
        "> This brief is ready for human messaging review. It is not permission to send.",
        "",
    ])
    return "\n".join(lines)
