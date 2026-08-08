from pathlib import Path
import importlib.util
from tempfile import TemporaryDirectory
import unittest

from abm_engine.library import SignalLibrary


ROOT = Path(__file__).resolve().parents[1]


INIT_SCRIPT = ROOT / "scripts" / "init_workspace.py"
INIT_SPEC = importlib.util.spec_from_file_location("init_workspace", INIT_SCRIPT)
INIT_MODULE = importlib.util.module_from_spec(INIT_SPEC)
assert INIT_SPEC.loader
INIT_SPEC.loader.exec_module(INIT_MODULE)


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

    def test_workspace_initializer_creates_blank_templates(self):
        with TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            created, skipped = INIT_MODULE.install_workspace(workspace)
            self.assertGreater(len(created), 0)
            self.assertEqual([], skipped)
            self.assertTrue((workspace / "templates/research-record.md").exists())
            self.assertTrue((workspace / "templates/evidence-record.json").exists())
            self.assertTrue((workspace / "templates/campaign-brief.json").exists())

    def test_industry_agnostic_pack_has_complete_portable_schema(self):
        library = SignalLibrary.from_json(ROOT / "data" / "industry-agnostic-signals.json")
        self.assertGreaterEqual(len(library.signals), 20)
        self.assertEqual(len(library.signals), len({signal.key for signal in library.signals}))
        for signal in library.signals:
            self.assertEqual("industry-agnostic-v1", signal.pack)
            self.assertTrue(signal.query_template)
            self.assertTrue(signal.applicability)
            self.assertTrue(signal.safe_interpretation)
            self.assertTrue(signal.prohibited_inference)
            self.assertTrue(signal.source_priority)
            self.assertTrue(signal.extracted_from)

    def test_natural_language_search_handles_key_separators(self):
        library = SignalLibrary.from_json(ROOT / "data" / "industry-agnostic-signals.json")
        keys = [signal.key for signal in library.search("product launch")]
        self.assertIn("public_product_launch", keys)


if __name__ == "__main__":
    unittest.main()
