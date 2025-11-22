from wordle_backend import *

def test_process_command_add_letter():
    game_state = {'secret_word': 'field', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 
                'colour_grid': [['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 0, 
                'j': 0, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': [], 
                'valid_words': [], 
                "wordle_words":[]}
    process_command(game_state, "g")
    assert (game_state['grid'], game_state['i'], game_state['j']) == ([['g', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], 0, 1)  
                          

