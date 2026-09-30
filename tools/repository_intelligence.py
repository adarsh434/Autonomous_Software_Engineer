from tools.repository_analyzer import analyze_repository
from tools.code_search import search_code
from tools.file_reader import read_file
from tools.code_structure import analyze_python_file

def get_repository_intelligence(repository_path: str, query: str | None = None, file_path: str | None = None):
    result = {"repository": analyze_repository(repository_path)}

    # Search relevant code if a query is provided
    if query:
        result["search_results"] = search_code(repository_path, query)

    # Read a specific file if requested
    if file_path:
        result["file"] = read_file(repository_path, file_path)

        # Analyze Python structure
        if file_path.endswith(".py"):
            result["structure"] = analyze_python_file(f"{repository_path}/{file_path}")

    return result