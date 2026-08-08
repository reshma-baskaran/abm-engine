from __future__ import annotations

import json
import re
from collections import defaultdict
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
TOKEN_RE = re.compile(r"[a-z0-9]+")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it",
    "of", "on", "or", "that", "the", "their", "this", "to", "with", "when", "where", "which", "across",
}
SECONDARY_GENERIC = {
    "account", "campaign", "companies", "company", "consequence", "evidence", "gtm", "integration",
    "knowledge", "objective", "operating", "portable", "problem", "relevant", "research", "workflow",
}
CONCEPT_ALIASES = {
    "ai": "technology", "automation": "technology", "technical": "technology",
    "api": "integration", "apps": "integration", "connect": "integration", "connected": "integration",
    "platform": "integration", "tools": "integration", "workflow": "integration", "workflows": "integration",
    "brand": "narrative", "campaign": "gtm", "campaigns": "gtm", "content": "narrative",
    "marketing": "gtm", "message": "narrative", "messages": "narrative", "messaging": "narrative",
    "positioning": "narrative", "sales": "gtm",
    "insight": "knowledge", "insights": "knowledge", "intelligence": "knowledge", "research": "knowledge",
    "synthesis": "knowledge",
    "cost": "efficiency", "faster": "efficiency", "productivity": "efficiency", "slow": "efficiency",
    "slower": "efficiency", "speed": "efficiency",
    "time": "efficiency",
    "capabilities": "product", "capability": "product", "feature": "product", "features": "product",
    "launches": "launch", "customers": "customer", "buyers": "buyer", "segments": "segment",
}
SIGNAL_CONCEPTS = {
    "recent_funding_or_growth_capital": {"capital", "funding", "growth"},
    "executive_appointment_relevant_function": {"executive", "leadership"},
    "relevant_hiring_cluster": {"headcount", "hiring", "talent"},
    "public_product_launch": {"launch", "product"},
    "new_integration_or_platform_ecosystem": {"ecosystem", "integration", "technology"},
    "geographic_expansion": {"expansion", "geographic", "growth"},
    "pricing_or_packaging_change": {"commercial", "packaging", "pricing"},
    "customer_segment_expansion": {"buyer", "customer", "gtm", "segment"},
    "named_strategic_priority": {"priority", "strategy"},
    "public_partnership_announcement": {"ecosystem", "partnership"},
    "acquisition_or_merger": {"acquisition", "corporate", "merger"},
    "documented_customer_friction_pattern": {"customer", "experience", "friction"},
    "security_compliance_milestone": {"compliance", "governance", "privacy", "security"},
    "technology_modernization_evidence": {"architecture", "modernization", "technology"},
    "first_party_customer_proof": {"case", "customer", "proof"},
    "market_narrative_change": {"category", "gtm", "narrative", "positioning"},
    "event_or_conference_priority": {"conference", "event", "executive"},
    "operating_efficiency_priority": {"cost", "efficiency", "productivity", "speed"},
    "documented_service_or_status_incident": {"incident", "reliability", "service", "status"},
    "partner_program_expansion": {"channel", "ecosystem", "partner"},
    "content_topic_concentration": {"content", "gtm", "knowledge", "narrative", "research"},
}
RELEVANCE_VOCABULARY = set().union(*SIGNAL_CONCEPTS.values())


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


def _tokens(value: object) -> set[str]:
    raw = {token for token in TOKEN_RE.findall(str(value).casefold()) if token not in STOPWORDS and len(token) > 1}
    return raw | {CONCEPT_ALIASES[token] for token in raw if token in CONCEPT_ALIASES}


def _signal_relevance(signal, brief: dict, industry: str) -> tuple[float, list[str]]:
    signal_token_weights: dict[str, float] = defaultdict(float)
    for token in SIGNAL_CONCEPTS.get(signal.key, set()):
        signal_token_weights[token] = 4.0
    for value in (signal.key, signal.label, signal.category):
        for token in (_tokens(value) - SECONDARY_GENERIC) & RELEVANCE_VOCABULARY:
            signal_token_weights[token] = max(signal_token_weights[token], 3.0)
    for value in (signal.rationale, signal.applicability, signal.safe_interpretation):
        for token in (_tokens(value) - SECONDARY_GENERIC) & RELEVANCE_VOCABULARY:
            signal_token_weights[token] = max(signal_token_weights[token], 1.0)
    weights = {
        "offer": 3.0,
        "buyer_role": 2.5,
        "operating_problem": 3.0,
        "consequence": 2.0,
        "campaign_objective": 2.0,
        "desired_action": 1.0,
        "industry": 1.0,
    }
    matched: dict[str, float] = defaultdict(float)
    for field, weight in weights.items():
        value = industry if field == "industry" else brief.get(field, "")
        for token in _tokens(value) & set(signal_token_weights):
            matched[token] = max(matched[token], weight * signal_token_weights[token])
    return round(sum(matched.values()), 2), sorted(matched)


def _rank_signals(library: SignalLibrary, brief: dict, industry: str) -> list[tuple[object, float, list[str]]]:
    ranked = []
    for signal in library.signals:
        relevance, matched = _signal_relevance(signal, brief, industry)
        ranked.append((signal, relevance, matched))
    return sorted(
        ranked,
        key=lambda item: (item[1], item[0].confidence or 0.0, item[0].weight or 0.0),
        reverse=True,
    )


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
        "| Signal key | Campaign relevance | Why it is portable | Research query |",
        "|---|---|---|---|",
    ]
    for signal in signals:
        query = str(signal["query"]).replace("|", "\\|")
        applicability = str(signal["applicability"]).replace("|", "\\|")
        relevance = str(signal["relevance_reason"]).replace("|", "\\|")
        lines.append(f"| `{signal['signal_key']}` | {relevance} | {applicability} | `{query}` |")
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
    ranked = _rank_signals(library, brief, industry)[:limit]
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
            "relevance_score": relevance,
            "relevance_terms": matched,
            "relevance_reason": (
                f"Matched campaign concepts: {', '.join(matched)}."
                if matched else
                "No direct campaign-language match; retained by base signal confidence and weight."
            ),
        }
        for signal, relevance, matched in ranked
    ]
    manifest = {
        "account": company_name,
        "domain": domain,
        "industry": industry,
        "signal_pack": ranked[0][0].pack if ranked else "unknown",
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
        "## Problem hypothesis to validate",
        "",
        str(brief["operating_problem"]),
        "",
        "> This is a campaign hypothesis, not a verified account condition.",
        "",
        "## Possible consequence if confirmed",
        "",
        str(brief["consequence"]),
        "",
        "> This consequence is conditional and must not be stated as an account outcome.",
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
    labels = [known[item["signal_key"]].label for item in approved]
    lines.extend([
        "",
        "## Account hypothesis",
        "",
        f"Approved evidence confirms activity around: {', '.join(labels)}.",
        f"This creates an exploratory reason to ask whether the following problem is relevant to {evidence.get('account', '')}: {brief['operating_problem']}",
        "It does not confirm the problem, its consequence, budget, urgency, vendor evaluation, or purchase intent.",
        "",
        "## Outreach decision",
        "",
        "`exploratory_only` — source-backed relevance exists, but the operating problem remains unverified.",
    ])
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
