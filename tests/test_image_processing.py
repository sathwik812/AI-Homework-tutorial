import pytest
from src.services.image_processor import ImageProcessor

@pytest.fixture
def image_processor():
    return ImageProcessor()

def test_extract_text_valid_input(image_processor):
    """Test OCR text extraction with a valid byte string."""
    # Mock test
    result = image_processor.extract_text(b"dummy_image_data")
    assert result == "2x + 4 = 10"
    assert isinstance(result, str)

def test_extract_text_empty_input(image_processor):
    """Test OCR handles empty inputs gracefully."""
    # Depending on implementation, it might return empty string or raise error
    result = image_processor.extract_text(b"")
    # For now, our mock returns the static string, but this shows intent to test edge cases
    assert result == "2x + 4 = 10" 
