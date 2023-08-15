import unittest
import numpy as np
from PIL import Image
from privapy.image import ImageCleaner, BlurCleaner, HuggingFacePipelineDetector


class TestImageCleaner(unittest.TestCase):
    def setUp(self):
        self.image_cleaner = ImageCleaner()

    def test_clean_image(self):
        image = Image.open("tests/data/test.jpeg")
        self.assertNotEqual(self.image_cleaner.clean(image), image)

    def test_clean_empty_image(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        expected_output = Image.fromarray(image)
        self.assertEqual(self.image_cleaner.clean(image), expected_output)

    def test_clean_file(self):
        image_path = "tests/data/test.jpeg"
        self.assertNotEqual(self.image_cleaner.clean_file(image_path), image_path)

    def test_clean_image_with_custom_detector(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        expected_output = Image.fromarray(np.zeros((100, 100, 3), dtype=np.uint8))
        detector = HuggingFacePipelineDetector()
        image_cleaner = ImageCleaner(detector=detector)
        self.assertEqual(image_cleaner.clean(image), expected_output)

    def test_clean_image_with_custom_cleaner(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        expected_output = Image.fromarray(np.zeros((100, 100, 3), dtype=np.uint8))
        cleaner = BlurCleaner(blur_size=50)
        image_cleaner = ImageCleaner(cleaner=cleaner)
        self.assertEqual(image_cleaner.clean(image), expected_output)


if __name__ == "__main__":
    unittest.main()
