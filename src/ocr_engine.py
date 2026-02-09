import pytesseract

def extract_text(processed_image):
    custom_config = "--oem 3 --psm 6"
    text = pytesseract.image_to_string(processed_image, config=custom_config)
    return text
