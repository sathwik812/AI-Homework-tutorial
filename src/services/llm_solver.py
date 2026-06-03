from src.models import HomeworkSolution, SolutionStep
from src.config import settings
import json
# import google.generativeai as genai

class LLMSolver:
    def __init__(self):
        # genai.configure(api_key=settings.gemini_api_key)
        # self.model = genai.GenerativeModel('gemini-2.5-flash')
        pass

    def solve(self, problem_text: str) -> HomeworkSolution:
        """Use LLM to solve the problem and output structured steps."""
        # TODO: Implement actual API calls with Chain-of-Thought
        return HomeworkSolution(
            problem_text=problem_text,
            solution_steps=[
                SolutionStep(step_number=1, explanation="Subtract 4 from both sides.", latex_equation="2x = 6"),
                SolutionStep(step_number=2, explanation="Divide by 2.", latex_equation="x = 3")
            ],
            final_answer="x = 3"
        )
