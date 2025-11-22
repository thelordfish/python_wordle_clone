from wordle_backend import *

def test_process_command_restart():
     
    save_file = Path(__file__).parent / "save_file.txt"
    if save_file.exists():                                                  #attempt to wipe the save file as it interferes, doesnt seem to work every time however
        save_file.unlink()

    game_state = {'secret_word': 'taste', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['h', 'e', 'l', 'l', 'o'], ['h', 'o', 'o', 'l', 'a'], ['s', 'n', 'i', 'p', 'e'], ['s', 'n', 'o', 'o', 'd'], ['s', 't', 'a', '', '']], 
                'colour_grid': [['g', 'y', 'g', 'g', '-'], ['-', 'y', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['y', '-', '-', '-', 'y'], ['y', '-', '-', '-', '-'], ['w', 'w', 'w', 'w', 'w']], 
                'i': 5, 
                'j': 3, 
                'status': 'playing', 
                'wordle_words_file': 
                'wordle_words.txt', 
                'all_words_file': 
                'english_dict.txt', 
                'popup_queue': [], 
                'active_letters': [], 
                'valid_words': ['testy', 'taste'], 
                "wordle_words":[]}
    
    restart(game_state)

    assert (game_state['word_length'], 
            game_state['max_guesses'], 
            game_state['grid'], 
            game_state['colour_grid'], 
            game_state['i'], 
            game_state['j'], 
            game_state['status'], 
            game_state['wordle_words_file'], 
            game_state['all_words_file']) == (
                       5, 
                       6, 
                       [['', '', '', '', ''], 
                        ['', '', '', '', ''], 
                        ['', '', '', '', ''], 
                        ['', '', '', '', ''], 
                        ['', '', '', '', ''], 
                        ['', '', '', '', '']], 
                        [['w', 'w', 'w', 'w', 'w'], 
                        ['w', 'w', 'w', 'w', 'w'], 
                        ['w', 'w', 'w', 'w', 'w'], 
                        ['w', 'w', 'w', 'w', 'w'], 
                        ['w', 'w', 'w', 'w', 'w'], 
                        ['w', 'w', 'w', 'w', 'w']], 
                        0, 
                        0, 
                        'playing',  
                        'wordle_words.txt', 
                        'english_dict.txt')
