from pydantic import BaseModel
from typing import Optional, List

class SolutionStep(BaseModel):
    step_number: int
    explanation: str
    latex_equation: Optional[str] = None

class HomeworkSolution(BaseModel):
    problem_text: str
    solution_steps: List[SolutionStep]
    final_answer: str
    audio_url: Optional[str] = None
    video_url: Optional[str] = None

class ErrorResponse(BaseModel):
    error: str
    details: Optional[str] = None
