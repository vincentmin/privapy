"""Base image method classes."""
from typing import List
import numpy as np


class BaseDetector:
    """Base class for detection methods."""

    def get_bounding_boxes(self, image: np.ndarray) -> List[np.ndarray]:
        """Detect objects in an image.

        Args:
            image (np.ndarray): Image to detect objects in.

        Returns:
            List[np.ndarray]: List of bounding boxes of detected objects. Format: [x1, y1, x2, y2]
        """
        raise NotImplementedError


class BaseCleaner:
    """Base class for image cleaning methods."""

    def clean(self, image: np.ndarray, bounding_boxes: List[np.ndarray]) -> np.ndarray:
        """Clean an image.

        Args:
            image (np.ndarray): Image to clean.
            bounding_boxes (List[np.ndarray]): List of bounding boxes of detected objects.

        Returns:
            np.ndarray: Cleaned image.
        """
        raise NotImplementedError
