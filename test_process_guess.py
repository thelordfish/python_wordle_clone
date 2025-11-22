from wordle_backend import *

def test_process_guess():
    game_state ={'secret_word': 'taste', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 
                'colour_grid': [['g', 'y', 'g', 'g', '-'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 5, 
                'j': 0, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': [], 
                'valid_words': ['testy'], 
                "wordle_words":[]}
    result = process_guess("testy", game_state)
    assert result==['g', 'y', 'g', 'g', '-'], f"process_guess() inaccurately changing colour list, should read g,y,g,g,- :{result}"

    