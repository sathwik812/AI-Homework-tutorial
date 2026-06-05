import pytest
from fastapi.testclient import TestClient
from src.app import app
import io

client = TestClient(app)

def test_health_check_returns_200():
    """Verify the API is healthy and reachable."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_solve_endpoint_integration():
    """End-to-end integration test for the /solve endpoint."""
    # Create a mock file to upload
    mock_file = io.BytesIO(b"fake image data")
    mock_file.name = "test_image.png"

    response = client.post(
        "/solve",
        files={"image": ("test_image.png", mock_file, "image/png")}
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Assert on expected schema and mocked values
    assert "problem_text" in data
    assert "solution_steps" in data
    assert "final_answer" in data
    assert "audio_url" in data
    
    assert data["final_answer"] == "x = 3"
    assert len(data["solution_steps"]) > 0

def test_solve_endpoint_missing_image():
    """Verify the API correctly handles missing required fields."""
    response = client.post("/solve")
    assert response.status_code == 422 # Unprocessable Entity (FastAPI default validation error)
