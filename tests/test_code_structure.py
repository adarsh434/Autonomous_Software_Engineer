from tools.code_structure import analyze_python_file


def test_analyze_python_file(tmp_path):

    file = tmp_path / "example.py"

    file.write_text(
        "class UserService:\n"
        "    def get_user(self, user_id):\n"
        "        pass\n"
        "\n"
        "def create_user(data):\n"
        "    pass\n"
    )

    result = analyze_python_file(str(file))

    assert len(result["classes"]) == 1
    assert result["classes"][0]["name"] == "UserService"

    assert len(
        result["classes"][0]["methods"]
    ) == 1

    assert (
        result["classes"][0]["methods"][0]["name"]
        == "get_user"
    )

    assert len(result["functions"]) == 1
    assert result["functions"][0]["name"] == "create_user"