import random 

class Hangman:
    def __init__(self, word_list, num_lives = 5):
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
        guess = input('Please enter a letter: ')
        if guess.isalpha() == False or len(guess) > 1:
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
        


def play_game(word_list):
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

