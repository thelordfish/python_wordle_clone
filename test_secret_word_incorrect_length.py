from wordle_backend import *

def test_secret_word_incorrect_length():
    try:
        check_inputs("taste", 3, 6, ['taste'])
        raise AssertionError("failed to raise Exception where len(secret_word) > word_length")
    except Exception as error :
        assert error 
    try:
        check_inputs("taste", 7, 6, ['taste'])
        raise AssertionError("failed to raise Exception where len(secret_word) < word_length")
    except Exception as error :
        assert error 