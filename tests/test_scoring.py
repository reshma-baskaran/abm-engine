import unittest

from abm_engine.scoring import Evidence, score_evidence


class ScoringTests(unittest.TestCase):
    def test_requires_evidence_and_source(self):
        item = Evidence("signal", 2.0, 4.0, 5.0, "", "Observed fact")
        self.assertEqual(0.0, item.contribution)

    def test_normalizes_mixed_confidence_scale(self):
        items = [
            Evidence("a", 2.0, 4.0, 5.0, "https://example.com/a", "Observed fact"),
            Evidence("b", 1.5, 0.8, 1.0, "https://example.com/b", "Observed fact"),
        ]
        self.assertEqual(2.8, score_evidence(items))


if __name__ == "__main__":
    unittest.main()

