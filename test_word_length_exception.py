from wordle_backend import *

def test_word_length_exception():
    try:
        check_inputs("taste", 0, 5, ['taste'])
        raise AssertionError("failed to raise Exception where word_length <0")
    except Exception as error :
        assert error 
  