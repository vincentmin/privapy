import unittest
import numpy as np
from PIL import Image
from privapy.image import HuggingFacePipelineDetector


class TestHuggingFacePipelineDetector(unittest.TestCase):
    def setUp(self):
        self.detector = HuggingFacePipelineDetector()

    def test_get_bounding_boxes(self):
        image = Image.open("tests/data/test.jpeg")
        self.assertTrue(len(self.detector.get_bounding_boxes(image)) > 0)

    def test_get_bounding_boxes_with_custom_labels(self):
        image = Image.fromarray(np.zeros((100, 100, 3), dtype=np.uint8))
        expected_output = []
        detector = HuggingFacePipelineDetector(labels=["car"])
        self.assertEqual(detector.get_bounding_boxes(image), expected_output)


if __name__ == "__main__":
    unittest.main()
