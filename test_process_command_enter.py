from wordle_backend import *

def test_process_command_enter():
    game_state = {'secret_word': 'taste', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 
                'colour_grid': [['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 0, 
                'j': 5, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': [], 
                'valid_words': ['testy'], 
                "wordle_words":[]}
    
    print(enter(game_state))

    assert game_state == {'secret_word': 'taste', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 
                'colour_grid': [['g', 'y', 'g', 'g', '-'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 1, 
                'j': 0, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': [], 
                'valid_words': ['testy'], 
                "wordle_words":[]}, f"Enter command failed to produce expected result. Should be i =1, j=0, [[]'t','e','s','t','y']..., [['g','y','g','g','-']... Game_state['colour_grid'] was: {game_state['colour_grid']}"