"""
File: hangman_extension.py
Name: Angel Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random
from time import sleep

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function keeps asking user to guess an alphabet.
    If the user answers correctly within N_TURNS times, the user wins;
    otherwise, the user loses the hangman game.
    """
    print("Let's play Hangman!")
    sleep(0.6)
    word = random_word()
    print(word)
    play(word)
    sleep(0.6)
    while input("\nPlay Again? (Y/N)").upper() == "Y":
        print("Let's play Hangman!")
        word = random_word()
        play(word)


def play(word):
    """
    This function asks user to guess letter,
    if user answers correctly within 7 times, the user wins;
    otherwise, they lose the game.
    :param word: str, the correct answer.
    :return: str, the game result--win or lose.
    """
    word_completion = "_" * len(word)
    guesses_letters = ''  # create an empty string to store the guessed and correct letters.
    tries = N_TURNS  # determine the number of turns
    display_words = word_completion   # display the current guessed letters

    # while loop : keep asking user to guess the letter
    while True:
        print("The word looks like: " + display_words)
        print("You have " + str(tries) + " guesses left.")
        guess = input("Your guess: ").upper()  # ask the user go guess a character
        if len(guess) == 1 and guess.isalpha():  # when user inputs one alphabet
            if guess not in word:  # if user guesses wrong alphabet
                print("There is no " + guess + "'s in the word.")
                tries -= 1  # then decrease the failed counter with one
                print(display_hangman(tries))  # print the hangman pic when user guesses wrong answer

            else:  # if user guesses correctly
                print("You are correct!")
                if guess not in guesses_letters:  # if this letter is not stored in the guessed_list
                    guesses_letters += guess  # then add this letter into guessed_list

                word_str = ""  # to store the temporary displayed word
                # two for loop: to decide how to display the words
                for i in range(len(word)):
                    char = word[i]
                    for j in range(len(guesses_letters)):
                        x = guesses_letters[j]
                        if char == x:  # if the letter is already guesses_letter
                            word_str += x  # then add this word to temporary displayed word
                    if char not in guesses_letters:
                        word_str += "_"
                display_words = word_str  # update the displayed words

        else:  # when user inputs more than one alphabet or other symbols
            print("Illegal format.")
        if display_words == word and tries > 0:
            print("\nHOORAY~~You win! \nThe word was " + word)
            break
        if tries == 0:
            print("You're completely hung ;( \nThe word was: " + word)
            break


def display_hangman(tries):
    if tries == 6:
        return """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    if tries == 5:
        return """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """
    if tries == 4:
        return """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """

    if tries == 3:
        return """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """
    if tries == 2:
        return """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """
    if tries == 1:
        return """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """
    if tries == 0:
        return """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -"""


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
