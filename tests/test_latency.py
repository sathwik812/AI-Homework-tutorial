import time
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.performance
def test_api_latency_health_check():
    """Ensure the health check endpoint responds within acceptable SLA (<50ms)."""
    start_time = time.time()
    response = client.get("/health")
    end_time = time.time()
    
    latency_ms = (end_time - start_time) * 1000
    assert response.status_code == 200
    assert latency_ms < 50, f"Health check latency too high: {latency_ms:.2f}ms"
