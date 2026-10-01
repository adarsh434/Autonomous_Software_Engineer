from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openrouter import ChatOpenRouter
from pydantic import BaseModel, Field
from enum import Enum


load_dotenv()

class ActionType(str, Enum):
    SEARCH_CODE = "search_code"
    READ_FILE = "read_file"
    ANALYZE_STRUCTURE = "analyze_structure"
    REPOSITORY_INTELLIGENCE = "repository_intelligence"

class PlanStep(BaseModel):
    action: ActionType
    query: str | None = Field(
        default=None,
        description="Search query if applicable"
    )
    file: str | None = Field(
        default=None,
        description="File path if applicable"
    )


class AgentPlan(BaseModel):
    task: str
    reasoning: str
    steps: list[PlanStep]

llm = ChatOpenRouter(
    model="stealth/space-bunny-alpha",
    temperature=0
)

planner = llm.with_structured_output(AgentPlan)


SYSTEM_PROMPT = """
You are the planning component of an autonomous software engineer.

Your job is to analyze a software engineering task and create
a structured investigation plan.

Available actions:

1. search_code
   Search for a keyword or phrase across the repository.

2. read_file
   Read a specific file or line range.

3. analyze_structure
   Analyze classes, methods and functions in a Python file.

4. repository_intelligence
   Get an overview of the repository.

Do not modify any code.

Create only the investigation steps necessary to understand
the software engineering task.

For search_code, provide a useful search query.

For read_file, provide the relevant file path.

For analyze_structure, provide the relevant Python file.

For repository_intelligence, no additional parameter is required.
"""


def create_plan(task: str) -> AgentPlan:

    messages = [
        (
            "system",
            SYSTEM_PROMPT
        ),
        (
            "human",
            task
        )
    ]

    return planner.invoke(messages)