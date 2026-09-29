from pathlib import Path


def search_code(repository_path: str, query: str, extension : str | None = None):

    root = Path(repository_path)

    if not root.exists():
        raise ValueError("Repository path does not exist")

    if not root.is_dir():
        raise ValueError("Repository path is not a directory")

    results = []

    ignored_directories = {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".idea",
        ".vscode"
    }

    for path in root.rglob("*"):

        if not path.is_file():
            continue

        relative_path = path.relative_to(root)

        if any(part in ignored_directories for part in relative_path.parts):
            continue
        if extension and path.suffix != extension:
            continue
        
        try:
            content = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        except Exception:
            continue

        for line_number, line in enumerate(content.splitlines(), start=1):
            if query.lower() in line.lower():

                results.append({
                    "file": str(relative_path),
                    "line": line_number,
                    "content": line.strip()
                })

    return results