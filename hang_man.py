""" Hangman, the game"""
import random
import os
import time

class Word:
    def __init__(self, name):
        self.name = name
        self.length = len(name)
        self.letters = self.what_letters()

    def what_letters(self):
        letters = {}
        position = 0
        for letter in self.name:
            if letter in letters:
                letters[letter].append(position)
            else:
                letters[letter] = [position]
            position += 1
        return letters

def the_game():
    game_points = 0
    while game_points < 6:

        new_letter = input('Introduce your letter guess: ')
        check_letter(new_letter)

        os.system('clear')
        if new_letter in guess_letters:
            print('Hey, you already said this one! See?')
        if new_letter not in guess_letters:
            guess_letters.append(new_letter)
            if new_letter in hidden_word.letters:
                print(random.choice(['Great!', 'Well done!', 'Ouh yesss!',
                                     'You think you are smart, ain\'t you?']))
            if new_letter not in hidden_word.letters:
                print(random.choice(['Man... This is going to hurt...',
                                     'Are you sure... I don\'t think so...',
                                     'Hey, hey, hey... "Hang" in there boy!',
                                     'Let\'s keep trying pal...']))
                game_points += 1
        print_game(game_points)
        the_word = print_the_word(guess_letters)
        print(game_points)


        if None not in the_word:
            os.system('clear')
            print_game(game_points)
            print_the_word(guess_letters)
            print('\n' * 3, '----> YOU WON! <----', '\n' * 2, 'Well done, the guy will live to see another day...\n\n')
            exit()

    os.system('clear')
    print_game(game_points)
    print('\n'*3, '----> GAME OVER <----', '\n'*2, 'Hope next time you save the guy...\n')

def check_letter(letter):
    while True:
        if letter.isalpha():
            if len(letter) == 1:
                break
        letter = input('Your guess needs to be a letter! Don\'t mess around and enter your guess ---> ')

def print_the_word(guesses):
    the_word = [None] * hidden_word.length
    for guess in guesses:
        if guess in hidden_word.letters:
            place = hidden_word.letters[guess]
            for j in place:
                the_word[j] = guess
    replacement = {'None':'__'}
    print(' ' * 5, end='')
    for i in the_word:
        if i == None:
            print('__ ', end='')
        else:
            print(i, ' ', end='')
    print('\n\n')
    return the_word

def print_game(points):
    print('Guesses so far --> ', guess_letters)

    if points == 0:
        print('''
      ============================== 
      ||    //                     |
      ||   //
      ||  //
      || //
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')

    if points == 1:
        print('''
      ============================== 
      ||    //                     |
      ||   //                     ###
      ||  //                     #o#o#
      || //                       #~#
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')

    if points == 2:
        print('''
      ============================== 
      ||    //                     |
      ||   //                     ###
      ||  //                     #o#o#
      || //                       #~#
      ||                           |
      ||                           |
      ||                           |
      ||                           |
      ||                           |
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')

    if points == 3:
        print('''
      ============================== 
      ||    //                     |
      ||   //                     ###
      ||  //                     #o#o#
      || //                       #~#
      ||                           |
      ||                           |
      ||                           |
      ||                           |
      ||                           |
      ||                          /
      ||                         /
      ||                        /
      ||                     __/
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')

    if points == 4:
        print('''
      ============================== 
      ||    //                     |
      ||   //                     ###
      ||  //                     #O#O#
      || //                       #O#
      ||                           |
      ||                           |
      ||                           |
      ||                           |
      ||                           |
      ||                          / \\
      ||                         /   \\
      ||                        /     \\
      ||                     __/       \\__
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')

    if points == 5:
        print('''
      ============================== 
      ||    //                     |
      ||   //                     ###
      ||  //                     #O#O#
      || //                       #O#
      ||                           |
      ||                          /|
      ||                         / |
      ||                        /  |
      ||                       /   |
      ||                      O   / \\
      ||                         /   \\
      ||                        /     \\
      ||                     __/       \\__
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')

    if points == 6:
        print('''
      ============================== 
      ||    //                     |
      ||   //                     ###
      ||  //                     #X#X#
      || //                       #O#
      ||                           |
      ||                          /|\\
      ||                         / | \\
      ||                        /  |  \\
      ||                       /   |   \\
      ||                      O   / \\  O
      ||                         /   \\
      ||                        /     \\
      ||                     __/       \\__
      ||
      ||
      ||
      ||
      ||
      ||
######################################################################
            ''')


hidden_word = Word(input('What is the word you want your friend to guess? --> '))
os.system('clear')

print('Let the game begin!\n\nWelcome, player!\nYou know how the HangMan works, right?\nThen go ahead and smash it!\n')
guess_letters = []
print_the_word(guess_letters)

the_game()