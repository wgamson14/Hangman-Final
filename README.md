# **Hangman** 

## **Contents**
  - 1: *Description*
  - 2: *Method*
  - 3: *Usage*

## **1: Description**

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## **2: Method**

### Milestone 2
Python was the main tool used for this section, creating basic lists and using an import to et the random function to enable to computer to pick a random word from our generated list.

### Milestone 3
Using python a *while loop* was created to iteratively check whether the user input met the criteria of alphabetic and single charactered. An *if* statement was used to check if the guess was present in the computer generated word. Two functions were then defined to allow these to be passed.

### Milestone 4 
Functions were wrapped around the *while loop* and *if* statement. Within the guess function it was checked the letter was in the word then a *for loop* was created to iterate over the computers choiice using the *enumerate* function then replacing the blank space if present. In the input function conditions were added to check if the letter was not a singular character or alphabetical, an *append* function was used to add the letter to a list of used letters.

### Milestone 5
A play game function added with conditions to complete the game, if lives reached 0 or if the word was guessed in its entirety.

## **3: Usage**

To simply use this code all that must be done is copy the contents of the file *milestone_5.py**, from the GitHub repository, into VSCode. Then run in the terminnal *python milestone_5.py* and simply ply the game as intended.


