""" Hangman, the game

GENERAL NOTES

Els espais son gratis, intenta posar mes espais entre blocs de if/for/while etc, per ferho mes visible simplement.
Python te una convencio en com escriure el codi (PEP8), no te cap efecte a nivell de performance, pero si
a nivell visual. Per exemple, 2 salts de linea al top/bottom de definicions de funcions i classes.
PyCharm et dona un avis al respecte. Intenta deixar el codi perfecte, q sempre vegis un "tick" de color verd
al PyCharm (cantonada superior dreta, just sobre la scroll bar).
"""
import os
import random


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


def check_letter(letter):
    while True:
        if letter.isalnum() and len(letter) == 1:
            break
        letter = input('Your guess needs to be a letter! Don\'t mess around and enter your guess ---> ')

    letter_list = accents(letter)
    return letter_list


def accents(letter):
    vocals = [
        ['a', 'à', 'á', 'â', 'ä'],
        ['e', 'è', 'é', 'ê', 'ë'],
        ['i', 'ì', 'í', 'î', 'ï'],
        ['o', 'ò', 'ó', 'ô', 'ö'],
        ['u', 'ù', 'ú', 'û', 'ü']
    ]

    letter_list = []

    for group in vocals:
        if letter in group:
            # COM: rename per claredat
            for char in group:
                if char in hidden_word.letters:
                    letter_list.append(char)
                # COM: innecessari - same same
                # if letter in group:
                #     for char in group:
                if char.upper() in hidden_word.letters:
                    letter_list.append(char.upper())

    # if letter_list == []:
    # COM: equivalent to
    if not letter_list:
        # Si no hi ha expressio, el if/while evalua bool(letter_list),
        # q dona False en casos de llistes/tuples/diccionaris buides
        letter_list = [letter]

    return letter_list


def print_game(points, the_word, guess_letters):
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

    # COM: fes servir elif en aquests casos, quan els if formen un group i son mutually exclusive
    # Estalvia algo de CPU
    # if points == 1:
    elif points == 1:
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

    elif points == 2:
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

    elif points == 3:
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

    elif points == 4:
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

    elif points == 5:
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

    elif points == 6:
        os.system('clear')
        print('\n', '----> GAME OVER! <----', '\n')
        print_the_word(hidden_word.what_letters())
        print('Hope next time you save the guy...')
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
        exit()

    if None not in the_word:
        os.system('clear')
        print('\n', '----> YOU WON! <----', '\n')
        print_the_word(guess_letters)
        print('Well done, the guy will live to see another day...')
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
        exit()


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
        # if key.isalnum() != True:
        # COM_1: comparacions amb booleans (incloent None) es fan usant l'operador "is"
        # if key.isalnum() is not True:
        # COM_2: tot i aixi, l'expressio es pot simplificar usant:
        if not key.isalnum():
            for i in hidden_word.letters[key]:
                the_word[i] = key

    print(' ' * 5, end='')

    for i in the_word:
        # COM: equivalent to
        # if i == None:
        if i is None:
            print('__ ', end='')
        else:
            print(i, ' ', end='')

    print('\n')
    return the_word


# COM: [va junt amb el comentari a final del codi]
# passa el arguments sempre q sigui possible, intenta evitar crides des de dins d'una funcio
# a variables a nivell global - quedaria aixi
# def the_game(hidden_word):
def the_game():
    game_points = 0
    guess_letters = []

    print_the_word(guess_letters)

    while game_points < 6:

        new_letter = check_letter(input('\nIntroduce your letter guess: '))
        os.system('clear')

        for letter in new_letter:
            if letter.lower() in guess_letters:
                print('Hey, you already said this one! See?')
                # COM: afegim "continue" per evitar indentacions a sota
                # El "continue" fa saltar el bucle for/while a la proxima iteracio - el pots
                # entendre com a un "break parcial"
                continue

            # if letter.lower() not in guess_letters:
            # COM_1: amb un else ja fem aqui, ja q les dues condicions son mutuament exclusives i nomes del tipus True o False
            # else:
            # COM_2: amb l'us de "continue" a dalt, no fa falta indentar tot el totxo de sota

            guess_letters.append(letter.lower())

            if letter in hidden_word.letters or letter.swapcase() in hidden_word.letters:
                print(random.choice(['Great!', 'Well done!', 'Ouh yesss!',
                                     'You think you are smart, ain\'t you kid?']), '\n')

            else:
                print(random.choice(['Man... This is going to hurt...',
                                     'Are you sure? I don\'t think so...',
                                     'Hey, hey, hey... "Hang" in there boy!',
                                     'Keep trying pal...']), '\n')
                game_points += 1

        the_word = print_the_word(guess_letters)
        print_game(game_points, the_word, guess_letters)


def initialize_the_game():
    game_option = input('Hey! It was about time to see you here!\nWhat modality of game do you want to play?\na) Player vs Player\nb) Player vs Machine\n--> ')

    while True:
        if game_option == 'a':
            # COM: mala idea fer servir el mateix nom per una variable en scope local i global
            word = input('\nGreat! What is the word you want your friend to guess? --> ')
            break

        elif game_option == 'b':
            print('\nThis option is currently not available. We are working on it so you can have fun soon...')
            exit()

        else:
            game_option = input('Nop, you only have 2 options:\na) Player vs Player\nb) Player vs Machine\n\nSo choose wisely...\n--> ')

    os.system('clear')

    print('Let the game begin!\n\nWelcome, player!\nYou know how the HangMan works, right?\nThen go ahead and smash it!\n')
    return word


hidden_word = Word(initialize_the_game())
the_game()

# COM: idealment, tot esta dins de classes o funcions excepte:
# 1) Imports
# 2) Constants
# 3) La crida de la funcio main()

# Hauria de quedar aixi (borrant les dues linies de sobre 398 i 399):
# def main():
#     hidden_word = Word(initialize_the_game())
#     the_game(hidden_word)
#
#
# main()

# Et deixo a tu q completis aquest punt!
