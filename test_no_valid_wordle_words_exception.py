import pytest
from wordle_backend import *

def test_no_valid_wordle_words_exception(tmp_path):
    
    empty_file = tmp_path / "empty.txt"  
    empty_file.write_text("")
    try:
        import_files("english_dict.txt", empty_file)
        raise AssertionError("import_files() failed to raise an exception for empty wordles file")
    except Exception as error :
        assert error 
   