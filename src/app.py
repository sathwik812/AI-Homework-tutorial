from fastapi import FastAPI, UploadFile, File, HTTPException
from prometheus_client import Counter, Histogram, Gauge
import time
import logging
from src.models import HomeworkSolution, ErrorResponse
from src.services.image_processor import ImageProcessor
from src.services.llm_solver import LLMSolver
from src.services.audio_generator import AudioGenerator

app = FastAPI(title="AI Homework Tutor", version="1.0.0")

# Metrics
request_count = Counter('homework_requests_total', 'Total requests')
latency = Histogram('homework_latency_seconds', 'Response latency')
accuracy_metric = Gauge('homework_accuracy', 'Current accuracy')

# Services
image_processor = ImageProcessor()
llm_solver = LLMSolver()
audio_generator = AudioGenerator()

logger = logging.getLogger(__name__)

@app.post("/solve", response_model=HomeworkSolution, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def solve_problem(image: UploadFile = File(...), problem_type: str = None):
    start = time.time()
    request_count.inc()
    
    try:
        image_bytes = await image.read()
        
        # 1. OCR
        problem_text = image_processor.extract_text(image_bytes)
        
        # 2. LLM Solving
        solution = llm_solver.solve(problem_text)
        
        # 3. TTS
        combined_explanation = " ".join([step.explanation for step in solution.solution_steps])
        audio_url = audio_generator.generate_audio(combined_explanation)
        solution.audio_url = audio_url
        
        return solution
        
    except Exception as e:
        logger.error(f"Error solving problem: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        latency.observe(time.time() - start)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
