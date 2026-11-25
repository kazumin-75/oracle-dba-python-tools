import importlib.util
from pathlib import Path

# ファイル名が数字で始まるので、パスから読み込む / Load by path because the file name starts with a digit
_path = Path(__file__).resolve().parent.parent / "exercises" / "01_basics.py"
_spec = importlib.util.spec_from_file_location("basics", _path)
basics = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(basics)


def test_count_words_ignores_case():
    assert basics.count_words("ORA-00600 ora-00600 ORA-04031") == {
        "ora-00600": 2,
        "ora-04031": 1,
    }


def test_count_words_empty():
    assert basics.count_words("") == {}
