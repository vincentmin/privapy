import unittest
import numpy as np
import cv2
from privapy.image.cleaner import BlurCleaner


class TestBlurCleaner(unittest.TestCase):
    def setUp(self):
        self.blur_cleaner = BlurCleaner()

    def test_clean_image(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        bounding_boxes = [np.array([10, 10, 20, 20])]
        expected_output = np.zeros((100, 100, 3), dtype=np.uint8)
        expected_output[10:20, 10:20] = cv2.blur(
            expected_output[10:20, 10:20], (25, 25)
        )
        self.assertTrue(
            np.array_equal(
                self.blur_cleaner.clean(image, bounding_boxes), expected_output
            )
        )

    def test_clean_image_with_custom_blur_size(self):
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        bounding_boxes = [np.array([10, 10, 20, 20])]
        expected_output = np.zeros((100, 100, 3), dtype=np.uint8)
        expected_output[10:20, 10:20] = cv2.blur(
            expected_output[10:20, 10:20], (50, 50)
        )
        blur_cleaner = BlurCleaner(blur_size=50)
        self.assertTrue(
            np.array_equal(blur_cleaner.clean(image, bounding_boxes), expected_output)
        )


if __name__ == "__main__":
    unittest.main()
