import random
word_list = ["apple", "orange", "watermelon", "strawberry", "kiwi"]     # Creating word list
print(word_list)
word = random.choice(word_list)      # Randomly generating one of the words from the word list
print(word)

guess = input("Please enter a letter: ")     # Asking the user for an input

if len(guess) == 1 and guess.isalpha():      # Verifying that the input is valid by checking its length and if its alphabetical 
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


