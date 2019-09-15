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

        new_letter = check_letter(input('Introduce your letter guess: '))

        os.system('clear')
        if new_letter in ['a', 'e', 'i', 'o', 'u']:
            new_letter_list = accents(new_letter)
        else:
            new_letter_list = [new_letter]

        for letter in new_letter_list:
            if letter.lower() in guess_letters:
                print('Hey, you already said this one! See?')
            if letter.lower() not in guess_letters:
                guess_letters.append(letter.lower())
                if letter in hidden_word.letters or letter.swapcase() in hidden_word.letters:
                    print(random.choice(['Great!', 'Well done!', 'Ouh yesss!',
                                         'You think you are smart, ain\'t you?']))
                else:
                    print(random.choice(['Man... This is going to hurt...',
                                         'Are you sure... I don\'t think so...',
                                         'Hey, hey, hey... "Hang" in there boy!',
                                         'Let\'s keep trying pal...']))
                    game_points += 1
        print_game(game_points)
        the_word = print_the_word(guess_letters)


        if None not in the_word:
            os.system('clear')
            print('''
      ============================== 
      ||    //                     |     
      ||   //                     """
      ||  //                                        "                       
      || //                                      " O "
      ||                                    ###   / "
      ||                                   #o#o# / "
      ||                                    #W# / "
      ||                             " O     |/ "
      ||                               " \\  /|
      ||                                " \\/ |
      ||                                  "  |
      ||                                     |
      ||                                    / \\ "
      ||                                   /   \\ "
      ||                                " /    / "
      ||                               " /    / "
      ||                              " /   " \\ "
      ||                              "  "     "
      ||                            
######################################################################

                        ''')

            print_the_word(guess_letters)
            print('\n' * 3, '----> YOU WON! <----', '\n' * 2, 'Well done, the guy will live to see another day...\n\n')
            exit()

    os.system('clear')
    print_game(game_points)
    print_the_word(hidden_word.what_letters())
    print('\n'*2, '----> GAME OVER <----', '\n'*2, 'Hope next time you save the guy...\n')

def check_letter(letter):
    while True:
        if letter.isalnum():
            if len(letter) == 1:
                return letter
                break
        letter = input('Your guess needs to be a letter! Don\'t mess around and enter your guess ---> ')

def accents(letter):
    letter_list = []
    if letter == 'a':
        for i in ['a', 'à', 'á', 'â', 'ä']:
            if i in hidden_word.letters:
                letter_list.append(i)
            if i.upper() in hidden_word.letters:
                letter_list.append(i.upper())
    if letter == 'e':
        for i in ['e', 'è', 'é', 'ê', 'ë']:
            if i in hidden_word.letters:
                letter_list.append(i)
            if i.upper() in hidden_word.letters:
                letter_list.append(i.upper())
    if letter == 'i':
        for i in ['i', 'ì', 'í', 'î', 'ï']:
            if i in hidden_word.letters:
                letter_list.append(i)
            if i.upper() in hidden_word.letters:
                letter_list.append(i.upper())
    if letter == 'o':
        for i in ['o', 'ò', 'ó', 'ô', 'ö']:
            if i in hidden_word.letters:
                letter_list.append(i)
            if i.upper() in hidden_word.letters:
                letter_list.append(i.upper())
    if letter == 'u':
        for i in ['u', 'ù', 'ú', 'û', 'ü']:
            if i in hidden_word.letters:
                letter_list.append(i)
            if i.upper() in hidden_word.letters:
                letter_list.append(i.upper())
    else:
        letter_list = [letter]
    return letter_list

def print_the_word(guesses):
    the_word = [None] * hidden_word.length
    for guess in guesses:
        if guess in hidden_word.letters:
            place = hidden_word.letters[guess]
            for j in place:
                the_word[j] = guess
        if guess.upper() in hidden_word.letters:
            place = hidden_word.letters[guess.upper()]
            for j in place:
                the_word[j] = guess.upper()
    for key in hidden_word.letters:
        if key.isalnum() != True:
            for i in hidden_word.letters[key]:
                the_word[i] = key
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