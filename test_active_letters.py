from wordle_backend import *

def test_active_letters():
    game_state ={'secret_word': 'taste', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 
                'colour_grid': [['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 5, 
                'j': 0, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 
                'valid_words': ['testy'], 
                "wordle_words":[]}
    process_guess("snood", game_state)
    assert game_state['active_letters'] == ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    