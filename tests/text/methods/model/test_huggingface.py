import unittest
from privapy.text.methods.model import HuggingFacePipeline


class TestHuggingFacePipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = HuggingFacePipeline()

    def test_replace_entities(self):
        text = "I live in New York and work at Google"
        expected_output = "I live in <<ENT>> and work at <<ENT>>"
        self.assertEqual(self.pipeline(text), expected_output)

    def test_replace_entities_with_custom_replacement(self):
        text = "I live in New York and work at Google"
        expected_output = "I live in [ENT] and work at [ENT]"
        pipeline = HuggingFacePipeline(replacement="[ENT]")
        self.assertEqual(pipeline(text), expected_output)


if __name__ == "__main__":
    unittest.main()
