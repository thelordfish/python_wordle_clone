from wordle_backend import *

def test_max_guesses_exception():
    try:
        check_inputs("taste", 5, 0, ['taste'])
        raise AssertionError("failed to raise Exception where max_guesses <0")
    except Exception as error :
        assert error 
  