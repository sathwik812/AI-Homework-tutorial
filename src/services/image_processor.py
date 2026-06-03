import io

class ImageProcessor:
    def __init__(self):
        pass
        
    def extract_text(self, image_bytes: bytes) -> str:
        """Extract text from the given image."""
        # TODO: Implement actual OCR logic (e.g. pytesseract, cloud APIs)
        return "2x + 4 = 10" # Mock extracted text
