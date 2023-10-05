import random
word_list = ["apple", "orange", "watermelon", "strawberry", "kiwi"]     # Creating word list
computer_choice = random.choice(word_list) 


def check_guess(guess):
    guess.lower()
    if guess in computer_choice:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
    
def ask_for_input():
    while True:
        guess = input('Please enter a letter: ')
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)


ask_for_input()
     

