from pathlib import Path


MAX_FILE_SIZE = 1_000_000


def read_file(
    repository_path: str,
    file_path: str,
    start_line: int = 1,
    end_line: int | None = None
):
    root = Path(repository_path).resolve()
    target = (root / file_path).resolve()

    if not target.exists():
        raise ValueError("File does not exist")

    if not target.is_file():
        raise ValueError("Path is not a file")

    try:
        target.relative_to(root)
    except ValueError:
        raise ValueError("File is outside the repository")

    if target.stat().st_size > MAX_FILE_SIZE:
        raise ValueError("File is too large")

    if start_line < 1:
        raise ValueError("start_line must be >= 1")

    if end_line is not None and end_line < start_line:
        raise ValueError("end_line must be >= start_line")

    try:
        content = target.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception as e:
        raise ValueError(f"Unable to read file: {e}")

    lines = content.splitlines()

    if end_line is None:
        end_line = len(lines)

    selected_lines = lines[start_line - 1:end_line]

    result = []

    for index, line in enumerate(
        selected_lines,
        start=start_line
    ):
        result.append({
            "line": index,
            "content": line
        })

    return {
        "file": file_path,
        "start_line": start_line,
        "end_line": min(end_line, len(lines)),
        "total_lines": len(lines),
        "content": result
    }