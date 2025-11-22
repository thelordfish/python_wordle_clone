import pytest
from wordle_backend import *


def test_no_valid_all_words_exception(tmp_path):
    empty_file = tmp_path / "empty.txt"  
    empty_file.write_text("")
    try:
        import_files(empty_file, "wordle_words.txt")
        raise AssertionError("import_files() failed to raise an exception for empty all_words_file")
    except Exception as error :
        assert error 
