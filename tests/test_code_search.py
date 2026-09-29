from tools.code_search import search_code

def test_search_code(tmp_path):

    file = tmp_path/"test.py"

    file.write_text(
        "def hello():\n"
        "    print('hello')\n"
    )

    results = search_code(
        str(tmp_path),
        "hello"
    )

    assert len(results) == 2
    assert results[0]["line"] == 1