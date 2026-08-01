from pathlib import Path
import unittest

from abm_engine.library import SignalLibrary


ROOT = Path(__file__).resolve().parents[1]


class SignalLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = SignalLibrary.from_markdown(ROOT / "data" / "signal-library.md")

    def test_verified_definition_count(self):
        self.assertEqual(866, len(self.library.signals))

    def test_verified_unique_key_count(self):
        self.assertEqual(858, self.library.stats()["unique_keys"])

    def test_scoped_keys_are_unique(self):
        scoped = [signal.scoped_key for signal in self.library.signals]
        self.assertEqual(len(scoped), len(set(scoped)))

    def test_query_rendering(self):
        signal = self.library.by_key("ai_initiative_press_release")[0]
        rendered = signal.render_query(company_name="Lowe's", company_domain="lowes.com", ticker="LOW")
        self.assertIn("Lowe's", rendered or "")
        self.assertNotIn("{{company_name}}", rendered or "")


if __name__ == "__main__":
    unittest.main()

