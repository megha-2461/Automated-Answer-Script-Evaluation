import cv2
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Failed to load image. Unsupported format or corrupted file.")

    return image
