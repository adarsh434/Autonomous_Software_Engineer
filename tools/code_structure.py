import ast
from pathlib import Path


def analyze_python_file(file_path: str):

    path = Path(file_path)

    if not path.exists():
        raise ValueError("File does not exist")

    if not path.is_file():
        raise ValueError("Path is not a file")

    try:
        source = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source)

    except SyntaxError as e:
        raise ValueError(
            f"Unable to parse Python file: {e}"
        )

    classes = []
    functions = []

    for node in tree.body:

        if isinstance(node, ast.FunctionDef):

            functions.append({
                "name": node.name,
                "line": node.lineno
            })

        elif isinstance(node, ast.AsyncFunctionDef):

            functions.append({
                "name": node.name,
                "line": node.lineno,
                "async": True
            })

        elif isinstance(node, ast.ClassDef):

            methods = []

            for child in node.body:

                if isinstance(
                    child,
                    (ast.FunctionDef, ast.AsyncFunctionDef)
                ):

                    method = {
                        "name": child.name,
                        "line": child.lineno
                    }

                    if isinstance(
                        child,
                        ast.AsyncFunctionDef
                    ):
                        method["async"] = True

                    methods.append(method)

            classes.append({
                "name": node.name,
                "line": node.lineno,
                "methods": methods
            })

    return {
        "file": str(path),
        "language": "python",
        "classes": classes,
        "functions": functions
    }