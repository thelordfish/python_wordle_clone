from wordle_backend import *

def test_lose():
     
    save_file = Path(__file__).parent / "save_file.txt"
    if save_file.exists():                                                  #attempt to wipe the save file as it interferes, doesnt seem to work every time however
        save_file.unlink()

    game_state = {'secret_word': 'taste', 
                'word_length': 5, 
                'max_guesses': 6, 
                'grid': [['t', 'e', 's', 't', 'y'], ['h', 'e', 'l', 'l', 'o'], ['h', 'o', 'o', 'l', 'a'], ['s', 'n', 'i', 'p', 'e'], ['s', 'n', 'o', 'o', 'd'], ['s', 't', 'a', 'r', 't']], 
                'colour_grid': [['g', 'y', 'g', 'g', '-'], ['-', 'y', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['y', '-', '-', '-', 'y'], ['y', '-', '-', '-', '-'], ['y', 'y', 'y', '-', 'y']], 
                'i': 6, 
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
    win_or_lose(['-','-','-','-','-'], game_state)
    assert game_state['status'] == 'lose', "win_or_lose() should have changed status to 'lose', but hasn't"

   

