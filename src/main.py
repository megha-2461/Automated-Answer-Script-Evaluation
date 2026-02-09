import cv2
import os

from image_loader import load_image
from preprocess import preprocess_image
from ocr_engine import extract_text

# ---------------- PATHS ---------------- #
RAW_IMAGE_PATH = "../data/raw_images/answer_script.webp"
PROCESSED_IMAGE_PATH = "../data/processed_images/answer_script_thresh.png"
TEXT_OUTPUT_PATH = "../data/extracted_text/answer_script.txt"

# Create folders if they don't exist
os.makedirs("../data/processed_images", exist_ok=True)
os.makedirs("../data/extracted_text", exist_ok=True)

# ---------------- PIPELINE ---------------- #
def main():
    print("Loading image...")
    image = load_image(RAW_IMAGE_PATH)

    print("Preprocessing image...")
    processed_image = preprocess_image(image)

    print("Saving processed image...")
    cv2.imwrite(PROCESSED_IMAGE_PATH, processed_image)

    print("Extracting text using OCR...")
    extracted_text = extract_text(processed_image)

    print("Saving extracted text...")
    with open(TEXT_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print("\nOCR COMPLETED SUCCESSFULLY ✅\n")
    print("------ Extracted Text ------\n")
    print(extracted_text)

if __name__ == "__main__":
    main()
