import pytest
from src.services.llm_solver import LLMSolver
from src.models import HomeworkSolution

@pytest.fixture
def llm_solver():
    return LLMSolver()

def test_llm_solve_basic_algebra(llm_solver):
    """Test that LLM solver handles basic algebra correctly and returns expected Pydantic schema."""
    problem = "2x + 4 = 10"
    solution = llm_solver.solve(problem)
    
    assert isinstance(solution, HomeworkSolution)
    assert solution.problem_text == problem
    assert solution.final_answer == "x = 3"
    assert len(solution.solution_steps) == 2
    assert solution.solution_steps[0].step_number == 1
    assert "Subtract 4" in solution.solution_steps[0].explanation

def test_llm_solve_empty_input(llm_solver):
    """Test LLM behavior when given an empty string."""
    solution = llm_solver.solve("")
    assert isinstance(solution, HomeworkSolution)
    # Ideally, we would test for an exception here in a real implementation
    assert solution.final_answer is not None
