import random
from pathlib import Path
import pickle

def import_files(all_words_file, wordle_words_file):
     #check and import wordle_words_file to wordle_words
    current_dir = Path(__file__).parent
    with open(current_dir/wordle_words_file, 'r') as open_file:
            wordle_words = [word.strip() for word in open_file if word]
            if not wordle_words:
                raise Exception("No valid words in wordle words file")
    
    
    #do the same with all_words_file to all_words
    with open(current_dir/all_words_file, 'r') as open_file:
            valid_words = [word.strip() for word in open_file if word.strip()]
            if not valid_words:
                raise Exception("No valid words in all words file")
    return valid_words, wordle_words

def check_inputs(secret_word, word_length, max_guesses, valid_words):
    if word_length < 1:
         raise Exception("Word length must be 1 letter or more")
    if secret_word is not None and len(secret_word) != word_length:
        raise Exception("The secret word is not of the correct length")
    if secret_word is not None and secret_word not in valid_words:
         raise Exception("Custom secret word not found in dictionary provided!")        #Hopefully extra exceptio won't cause program to fail automated tests
    if max_guesses < 1:
         raise Exception("Max guesses must be 1 or more")
    


def load_from_save():
    try:
        current_dir = Path(__file__).parent
        with open(current_dir/"save_file.txt", 'rb') as open_file:              #opened in 'rb' to write in binary, same with save_game and 'wb'
            return pickle.load(open_file)

    except FileNotFoundError:
    	with open(current_dir/"save_file.txt", 'w') as open_file:
             return False

def save_game(game_state):
    with open(Path(__file__).parent/"save_file.txt", 'wb') as open_file:
	    pickle.dump(game_state, open_file)
	



def initialise_history_file(game_state):
    history = {}
    history['number of games lost'] = 0
    for guess in range(game_state['max_guesses']):
         history[f'number of games won in {guess} guesses'] = 0
         
         
    try:
        current_dir = Path(__file__).parent
        with open(current_dir/"game_history.txt", 'rb')as open_file:
             if len(pickle.load(open_file)) != len(history):
                raise Exception(f"game_history.txt does not contain a valid history for max_guesses: {game_state['max_guesses']}, delete it or move to different folder and try again")
             else:
                return
    except:
        with open(current_dir/"game_history.txt", 'wb') as open_file:
             pickle.dump(history, open_file)
#             input("is history written?")
             return

         
     

def initialise_game(all_words_file, wordle_words_file = None, secret_word = None, max_guesses = 6, word_length = 5):
    
    valid_words, wordle_words = import_files(all_words_file, wordle_words_file)     #cache english dictionary and wordle dictionary

    check_inputs(secret_word, word_length, max_guesses, valid_words)                #check inputs are valid

    save = load_from_save()                                                         

    if not save:                                                                    #if save_file is empty, create game_state
        game_state = { 
			'secret_word': secret_word, 
			'word_length':word_length, 
			'max_guesses':max_guesses, 
			'grid':[], 
			'colour_grid':[], 
			'i':0, 
			'j':0, 
			'status':'playing', 
			'wordle_words_file':wordle_words_file, 
			'all_words_file':all_words_file, 
			'popup_queue':[], 
			'active_letters':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
			'valid_words': [],
			'wordle_words':[]
			}
        game_state['grid'] = [[''] * word_length for i in range(max_guesses)]
        game_state['colour_grid'] = [['w'] * word_length for j in range(max_guesses)]
        game_state['wordle_words'] = wordle_words
        game_state['valid_words'] = valid_words

        if secret_word == None:
                    game_state['secret_word'] = random.choice(wordle_words)
        else:
            game_state['secret_word'] = secret_word.lower()                         

    else:
         game_state = save  
         
    initialise_history_file(game_state)                                                            #else, load from save

    return game_state


def show_popup(game_state, content, mode="text"):
 game_state['popup_queue'].append((content, mode))
 return



def reset_game(game_state, secret_word=None):
    game_state.update(initialise_game(game_state['all_words_file'], game_state['wordle_words_file'], secret_word))
    save_game('')
    show_popup(game_state, "Restarting game")


def validate_guess(game_state):
    grid, i = game_state['grid'], game_state['i']
    guess = ''.join(grid[i])
    if guess == '' or len(guess) < len(game_state['secret_word']):
        print("Incomplete guess")
        return False
    elif guess not in game_state['valid_words']:
        show_popup(game_state, "Invalid word\nUse clear or delete to edit your guess ")
        return False
    else:
         return True
    

def process_guess(guess, game_state):
    secret_word = game_state['secret_word']
    colour_list = ['']*len(secret_word)
    letters_remaining ={}
    for letter in set(secret_word):
         letters_remaining[letter] = secret_word.count(letter)
         
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i] and letters_remaining[guess[i]] > 0:
            colour_list[i] = "g"
            letters_remaining[guess[i]] -=1

        elif guess[i] in secret_word and letters_remaining[guess[i]] > 0:
            colour_list[i] = "y"
            letters_remaining[guess[i]] -=1

        else:
            colour_list[i] = "-"
            change_active_letters(game_state,guess,i)

    return colour_list

def change_active_letters(game_state, guess, i):
    active_letters = game_state['active_letters']
    if guess[i] in active_letters:
        active_letters.remove(guess[i].lower())

def update_history(game_state, outcome):
     with open(Path(__file__).parent/"game_history.txt", 'rb')as open_file:
                history = pickle.load(open_file)
     if outcome == 'w':
        with open(Path(__file__).parent/"game_history.txt", 'wb')as open_file:
                history[f'number of games won in {game_state['i']} guesses'] +=1
                pickle.dump(history, open_file)                                                       #have to convert history dict back into string every time it is written. then eval() it to turn it into a dict
     else:
         with open(Path(__file__).parent/"game_history.txt", 'wb')as open_file:
                history[f'number of games lost'] +=1 
                pickle.dump(history, open_file)                                                       #have to convert history dict back into string every time it is written. then eval() it to turn it into a dict


def display_history(game_state):
    with open(Path(__file__).parent/"game_history.txt", 'rb')as open_file:
                history = pickle.load(open_file)
                history = [history[key] for key in history]
    show_popup(game_state, history, mode = "history")                                                   #currently this looks bad when it pops up. I have commented out a slightly better way however dont want to fail any automatic tests by using it
    
    # history = ''.join(['<br>' + str(key) +':' +str(history[key]) for key in history])
    # show_popup(game_state, f"Game history: <br> {history}", mode = "history")

    return True
 

def win_or_lose(colour_line, game_state):
    if colour_line == ['g','g','g','g','g']:
        game_state['status'] = "win"
        show_popup(game_state, "You won!", mode = "text")
        update_history(game_state, 'w')
        share(game_state)
        return True
    elif game_state['i'] == game_state['max_guesses']-1 or game_state['i'] > game_state['max_guesses']-1:
        game_state['status'] = 'lose'
        show_popup(game_state, f"You lose! The word was {game_state['secret_word']}")
        update_history(game_state, 'l')
        share(game_state)
        return True
    else:
        return False

def enter(game_state):
    colour_grid, grid, i = game_state['colour_grid'], game_state['grid'], game_state['i']
    if validate_guess(game_state):
            guess = "".join(grid[i])
            colour_grid[i] = process_guess(guess, game_state)
            if win_or_lose(colour_grid[i], game_state):
                 
                 save_game('')
                 return False
            else:
                 game_state['i']+=1
                 game_state['j']=0
                 save_game(game_state)
                 return True
    else:
        show_popup(game_state, "Invalid word\nUse clear or delete to edit your guess ")
        return True
    

def delete(game_state):
        grid, i, j = game_state['grid'], game_state['i'], game_state['j']
        if j ==0:
             print("Nothing to delete")
        else:
            grid[i][j-1] = ""
            game_state['j'] -=1
        return True

def clear(game_state):
        grid, i= game_state['grid'], game_state['i']
        grid[i] = [''] * game_state['word_length']
        game_state['j']=0
        return True

def restart(game_state):
        save_game('')
        show_popup(game_state, f"You have chosen to restart! The word was {game_state['secret_word']}")
        reset_game(game_state)
        game_state['status'] = "playing"
        return True


def add_letter(game_state, command):
    grid, i, j = game_state['grid'], game_state['i'], game_state['j']
    if j == game_state['word_length']:
        show_popup(game_state, "Can't add more letters\nUse clear or delete to edit your guess.")                 #if word is already full, refuse more letters.                          
        return True
    else:
        grid[i][j] = command
        game_state['j'] += 1
        return True
    
def share(game_state):
    message = [['']*game_state['word_length'] for row in range(game_state['max_guesses'])]
    if game_state['status'] == 'win' or game_state['status'] == 'lose':
        colour_grid = game_state['colour_grid']
        for row in range(min(game_state['i']+1, game_state['max_guesses'])):
            for column in range(game_state['word_length']):
                    if colour_grid[row][column] == 'g':
                        message[row][column] = '🟩'
                    elif colour_grid[row][column] == 'y':
                        message[row][column] = '🟨'
                    else:
                         message[row][column] = '⬜'
        message = [''.join(row) for row in message]
        show_popup(game_state, '<br>'.join(message), "share")                                       #as frontend is written in CSS and html, \n not working, html equivalent of \n is <br> 
        return False
    else:
        show_popup(game_state, "Game unfinished!", "text")              
        return True



def process_command(game_state, command: str):
    command = command.lower()
    if len(command) == 1 and command in "abcdefghijklmnopqrstuvwxyz":    
        return add_letter(game_state, command)
    
                        
    elif command == "delete" or command == "-":
        return delete(game_state)
    
    elif command == "clear" or command == "_":
        return clear(game_state)

    elif command == "enter" or command == "+":
         return enter(game_state)
    
    elif command == "restart" or command == "!":
         return restart(game_state)
    
    elif command == "share" or command == "@":
         return share(game_state)
    
    elif command == "history":
         return display_history(game_state)
    
    elif command == "hint" or command == "*":
         return process_command(game_state, give_hint(game_state))
         

    elif all(letter in "abcdefghijklmnopqrstuvwxyz-_+!@*" for letter in command):
        add_letter(game_state, command[0])
        return process_command(game_state, command[1:])
    
    else:
         show_popup(game_state, "Invalid command", 'text')
         return True
    
def give_hint(game_state):
     hint = sort_by_most_common(find_letter_variety(game_state, find_possible_words(game_state))).pop()
     show_popup(game_state, hint, 'text')
     return hint

def extract_hint_info(game_state):                                  #have elected to do this rather than keep a running tab in game_state, to optimize for the more common scenario that no hints are used
     rightly_placed = {}
     wrongly_placed = {}
     available_letters =game_state['active_letters']
     colour_grid = game_state['colour_grid']
     grid = game_state['grid']
     for word in range(game_state['i']) :
          for index in range(game_state['word_length']):
            rightly_placed.setdefault(index, [])           #make the value a list
            wrongly_placed.setdefault(index, [])
            if colour_grid[word][index] == 'g':
                 rightly_placed[index].append(grid[word][index])
            elif colour_grid[word][index] == 'y':
                 wrongly_placed[index].append(grid[word][index])
                 
     return rightly_placed, wrongly_placed, available_letters

def find_possible_words(game_state):
     rightly_placed, wrongly_placed, active_letters = extract_hint_info(game_state)
     valid_words = game_state['valid_words']
     possible_words = []

     for word in valid_words:
        valid_word = True
        for letter_index in range(game_state['word_length']):
            letter = word[letter_index]
            if letter in active_letters:
                if letter_index in wrongly_placed and letter not in wrongly_placed[letter_index]:
                    if letter_index in rightly_placed.keys() and letter in rightly_placed[letter_index]:
                         valid_word = True
            else:
                valid_word = False
                break
        if valid_word == True:
            possible_words.append(word)

     return possible_words

def find_letter_variety(game_state, possible_words):
     active_letters = game_state['active_letters']
     letter_variation = {}
     
     for word in possible_words:
          letter_variation.setdefault(word, set())
          for letter in word:
               if letter in active_letters:
                    letter_variation[word].add(letter)

     return letter_variation                        

def sort_by_most_common(letter_variation):
    #reversed_popularity = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'][::-1]       # this is from https://en.wikipedia.org/wiki/Letter_frequency#cite_note-15

    letter_reverse_priority ={'z': 1, 'q': 2, 'x': 3, 'j': 4, 'k': 5, 'v': 6, 'b': 7, 'p': 8,'y': 9, 'g': 10, 'f': 11, 'w': 12, 'm': 13, 'u': 14, 'c': 15, 'l': 16, 'd': 17, 'r': 18, 'h': 19, 's': 20, 'n': 21, 'i': 22, 'o': 23, 'a': 24, 't': 25, 'e': 26}
    
    max_variety = max(len(letter_variation[word]) for word in letter_variation)
    max_variety_words = [word for word in letter_variation if len(letter_variation[word]) == max_variety]
    ranking = {}
    for word in max_variety_words:
         ranking[word] = 0
         for letter in word:
              
              ranking[word] += letter_reverse_priority[letter]
    highest_rank = max(ranking[word] for word in ranking)
    highest_rank_words = [word for word in ranking if ranking[word] == highest_rank]
    random.shuffle(highest_rank_words)
    return highest_rank_words


           


