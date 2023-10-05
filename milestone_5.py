import random 

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        """
        The function initializes a Hangman game with a given word list and number of lives, and sets up
        the initial state of the game.
        
        :param word_list: The `word_list` parameter is a list of words from which the computer will
        randomly choose a word for the game. Each word in the list should be a string
        :param num_lives: The `num_lives` parameter is used to specify the number of lives or guesses
        the player has in the game. By default, it is set to 5 if no value is provided when creating an
        instance of the class, defaults to 5 (optional)
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.computer_choice = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.computer_choice)
        self.num_letters = len(self.word_guessed)
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.computer_choice:
            print(f'Good guess! {guess} is in the word.')
            for index in range(len((self.computer_choice))):
                if guess == self.computer_choice[index]:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
                    print(self.word_guessed)
                    
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives remaining.')
            print(self.word_guessed)
            

    def ask_for_input(self):
        """
        The function asks the user for input, checks if it is a valid letter, and then checks if the letter
        has already been guessed.
        """
        guess = input('Please enter a letter: ')
        if guess.isalpha() == False or len(guess) > 1:
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
        


def play_game(word_list):
    """
    The function `play_game` plays a game of Hangman using a given word list until the player either
    wins or loses.

    -------------------------------------------------------------------------------------------------

    parameters: 
    - word_list: The `word_list` parameter is a list of words that will be used in the Hangman
    game. Each word in the list represents a possible word that the player needs to guess

    """
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else: 
            print('Congratulations. You won the game!')
            break
            

word_list = ['paris', 'london', 'madrid', 'helsinki', 'rome', 'lisbon', 'stockholm', 'berlin',  'warsaw', 'vienna', 'zagreb']
play_game(word_list)

