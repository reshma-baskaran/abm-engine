from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SIGNAL_RE = re.compile(
    r"^- \*\*`(?P<key>[^`]+)`\*\*\s+—\s+(?P<body>.+)$"
)
WEIGHT_RE = re.compile(r"\bWeight(?:\s*:)?\s*(?P<value>\d+(?:\.\d+)?)", re.I)
CONFIDENCE_RE = re.compile(r"\bConf(?:idence)?(?:\s*:)?\s*(?P<value>\d+(?:\.\d+)?)", re.I)
QUERY_RE = re.compile(r"\bQuery:\s*`(?P<value>[^`]+)`", re.I)
RATIONALE_RE = re.compile(r"\*Rationale:\*\s*(?P<value>.+?)(?:\s*$)", re.I)


@dataclass(frozen=True)
class Signal:
    key: str
    label: str
    industry: str
    sub_industry: str
    category: str
    weight: float | None
    confidence: float | None
    query_template: str | None
    rationale: str | None
    source_line: int
    applicability: str | None = None
    disqualifiers: tuple[str, ...] = ()
    source_priority: tuple[str, ...] = ()
    freshness_days: int | None = None
    safe_interpretation: str | None = None
    prohibited_inference: str | None = None
    extracted_from: tuple[str, ...] = ()
    pack: str = "legacy"

    @property
    def scoped_key(self) -> str:
        return "::".join((self.industry, self.sub_industry, self.key))

    def render_query(self, **variables: str) -> str | None:
        if not self.query_template:
            return None
        rendered = self.query_template
        for name, value in variables.items():
            rendered = rendered.replace("{{" + name + "}}", value)
        return rendered

    def to_dict(self) -> dict:
        result = asdict(self)
        result["scoped_key"] = self.scoped_key
        return result


class SignalLibrary:
    def __init__(self, signals: Iterable[Signal]):
        self.signals = tuple(signals)

    @classmethod
    def from_markdown(cls, path: str | Path) -> "SignalLibrary":
        industry = "Unscoped"
        sub_industry = "Unscoped"
        category = "Uncategorized"
        signals: list[Signal] = []

        for number, raw_line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
            line = raw_line.strip()
            if line.startswith("# INDUSTRY:"):
                industry = line.split(":", 1)[1].strip()
                continue
            if line.startswith("## Sub-Industry:"):
                sub_industry = line.split(":", 1)[1].strip()
                continue
            if line.startswith("### "):
                category = line[4:].strip()
                continue

            match = SIGNAL_RE.match(line)
            if not match:
                continue

            body = match.group("body")
            label = re.split(r"\.\s+(?:Weight|Conf|Query|Detection|\*Rationale)", body, maxsplit=1)[0].strip().rstrip(".")
            weight_match = WEIGHT_RE.search(body)
            confidence_match = CONFIDENCE_RE.search(body)
            query_match = QUERY_RE.search(body)
            rationale_match = RATIONALE_RE.search(body)
            signals.append(
                Signal(
                    key=match.group("key"),
                    label=label,
                    industry=industry,
                    sub_industry=sub_industry,
                    category=category,
                    weight=float(weight_match.group("value")) if weight_match else None,
                    confidence=float(confidence_match.group("value")) if confidence_match else None,
                    query_template=query_match.group("value") if query_match else None,
                    rationale=rationale_match.group("value").rstrip("*").strip() if rationale_match else None,
                    source_line=number,
                )
            )
        return cls(signals)

    @classmethod
    def from_json(cls, path: str | Path) -> "SignalLibrary":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        raw_signals = payload.get("signals") if isinstance(payload, dict) else None
        if not isinstance(raw_signals, list):
            raise ValueError("signal pack must contain a signals array")
        signals: list[Signal] = []
        for number, item in enumerate(raw_signals, 1):
            if not isinstance(item, dict):
                raise ValueError(f"signal {number} must be an object")
            required = ("key", "label", "category", "query_template", "applicability", "safe_interpretation", "prohibited_inference")
            missing = [field for field in required if not str(item.get(field, "")).strip()]
            if missing:
                raise ValueError(f"signal {number} is missing: {', '.join(missing)}")
            signals.append(
                Signal(
                    key=str(item["key"]),
                    label=str(item["label"]),
                    industry=str(payload.get("industry", "Industry agnostic")),
                    sub_industry=str(payload.get("sub_industry", "Portable")),
                    category=str(item["category"]),
                    weight=float(item["weight"]),
                    confidence=float(item["confidence"]),
                    query_template=str(item["query_template"]),
                    rationale=str(item.get("rationale", "")) or None,
                    source_line=number,
                    applicability=str(item["applicability"]),
                    disqualifiers=tuple(str(value) for value in item.get("disqualifiers", [])),
                    source_priority=tuple(str(value) for value in item.get("source_priority", [])),
                    freshness_days=int(item["freshness_days"]),
                    safe_interpretation=str(item["safe_interpretation"]),
                    prohibited_inference=str(item["prohibited_inference"]),
                    extracted_from=tuple(str(value) for value in item.get("extracted_from", [])),
                    pack=str(payload.get("pack", "industry-agnostic")),
                )
            )
        return cls(signals)

    def search(self, text: str = "", *, industry: str = "", category: str = "") -> list[Signal]:
        needle = text.casefold()
        industry_needle = industry.casefold()
        category_needle = category.casefold()
        return [
            signal
            for signal in self.signals
            if (not needle or needle in " ".join((signal.key, signal.label, signal.rationale or "")).casefold())
            and (not industry_needle or industry_needle in signal.industry.casefold())
            and (not category_needle or category_needle in signal.category.casefold())
        ]

    def by_key(self, key: str) -> list[Signal]:
        return [signal for signal in self.signals if signal.key == key]

    def stats(self) -> dict[str, int]:
        return {
            "definitions": len(self.signals),
            "unique_keys": len({signal.key for signal in self.signals}),
            "industries": len({signal.industry for signal in self.signals}),
            "sub_industries": len({(signal.industry, signal.sub_industry) for signal in self.signals}),
            "categories": len({signal.category for signal in self.signals}),
            "query_templates": sum(signal.query_template is not None for signal in self.signals),
        }
