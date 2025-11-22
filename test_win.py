from wordle_backend import *

def test_win():
    game_state = {'secret_word': 'testy', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 
                'colour_grid': [['g', 'g', 'g', 'g', 'g'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 0, 
                'j': 4, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': [], 
                'valid_words': ['testy', 'taste'], 
                "wordle_words":[]}
    win_or_lose(['g','g','g','g','g'], game_state)
    assert game_state['status'] == 'win', "win_or_lose() should have changed status to 'win' but hasn't"

   

