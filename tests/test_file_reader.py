from tools.file_reader import read_file


def test_read_file(tmp_path):

    file = tmp_path / "example.py"

    file.write_text(
        "line 1\n"
        "line 2\n"
        "line 3\n"
        "line 4\n"
        "line 5\n"
    )

    result = read_file(
        str(tmp_path),
        "example.py",
        2,
        4
    )

    assert result["start_line"] == 2
    assert result["end_line"] == 4
    assert result["total_lines"] == 5

    assert result["content"][0]["line"] == 2
    assert result["content"][0]["content"] == "line 2"

    assert result["content"][2]["line"] == 4
    assert result["content"][2]["content"] == "line 4"