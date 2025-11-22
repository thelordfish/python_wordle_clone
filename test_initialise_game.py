from wordle_backend import initialise_game
from pathlib import Path

def test_initialise_game():
 
 
    
    save_file = Path(__file__).parent / "save_file.txt"
    if save_file.exists():
        save_file.unlink()

          
    game_state = initialise_game("english_dict.txt", "wordle_words.txt", "field" )
    result = game_state
    assert (game_state['secret_word'], 
            game_state['word_length'], 
            game_state['max_guesses'], 
            game_state['grid'], 
            game_state['colour_grid'], 
            game_state['i'], 
            game_state['j'], 
            game_state['status'], 
            game_state['wordle_words_file'], 
            game_state['all_words_file']) == ('field',
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
