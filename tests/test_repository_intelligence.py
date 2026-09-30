from tools.repository_intelligence import get_repository_intelligence


def test_repository_intelligence(tmp_path):
    test_file = tmp_path / "app.py"

    test_file.write_text(
        """
def hello():
    return "hello"
"""
    )

    result = get_repository_intelligence(
        str(tmp_path),
        query="hello",
        file_path="app.py"
    )

    assert result["repository"]["total_files"] == 1
    assert len(result["search_results"]) == 1
    assert result["structure"]["functions"][0]["name"] == "hello"