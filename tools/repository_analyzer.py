from pathlib import Path

IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".idea",
    ".vscode"
}
LANGUAGE_EXTENSIONS = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".jsx": "JavaScript",
    ".java": "Java",
    ".cpp": "C++",
    ".cc": "C++",
    ".c": "C",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP"
}

def detect_languages(files):
    languages = {}

    for file in files:
        extension = Path(file).suffix.lower()

        if extension in LANGUAGE_EXTENSIONS:
            language = LANGUAGE_EXTENSIONS[extension]
            languages[language] = languages.get(language, 0) + 1

    return languages

def analyze_repository(repository_path: str):
    root = Path(repository_path)

    if not root.exists():
        raise ValueError("Repository path does not exist")

    if not root.is_dir():
        raise ValueError("Repository path is not a directory")

    files = []

    for path in root.rglob("*"):

        if not path.is_file():
            continue

        relative_path = path.relative_to(root)

        if any(
            part in IGNORED_DIRECTORIES
            for part in relative_path.parts
        ):
            continue

        files.append(str(relative_path))

    return {
        "name": root.name,
        "files": sorted(files),
        "total_files": len(files),
        "languages": detect_languages(files)
    }