import unittest
from privapy.text.methods.model import HuggingFacePipeline


class TestHuggingFacePipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = HuggingFacePipeline()

    def test_replace_entities(self):
        text = "I live in New York and work at Google"
        cleaned_text = self.pipeline(text)
        self.assertNotEqual(cleaned_text, text)
        self.assertTrue("<<ENT>>" in cleaned_text)

    def test_replace_entities_with_custom_replacement(self):
        text = "I live in New York and work at Google"
        pipeline = HuggingFacePipeline(replacement="[ENT]")
        cleaned_text = pipeline(text)
        self.assertNotEqual(cleaned_text, text)
        self.assertTrue("[ENT]" in cleaned_text)


if __name__ == "__main__":
    unittest.main()
