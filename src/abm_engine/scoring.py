from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    signal_key: str
    weight: float
    confidence: float
    confidence_scale: float
    source_url: str
    evidence: str

    @property
    def contribution(self) -> float:
        if not self.source_url or not self.evidence.strip():
            return 0.0
        if self.confidence_scale <= 0:
            raise ValueError("confidence_scale must be positive")
        normalized = min(1.0, max(0.0, self.confidence / self.confidence_scale))
        return round(self.weight * normalized, 3)


def score_evidence(items: list[Evidence]) -> float:
    """Score only evidence that has both a source and a concrete observation."""
    return round(sum(item.contribution for item in items), 3)

