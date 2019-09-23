""" Hangman, the game"""
import random
import os


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


def check_letter(letter, hidden_word):
    while True:
        if letter.isalnum() and len(letter) == 1:
            break
        letter = input('Your guess needs to be a letter! Don\'t mess around and enter your guess ---> ')

    letter_list = accents(letter, hidden_word)
    return letter_list


def accents(letter, hidden_word):
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
            for char in group:
                if char in hidden_word.letters:
                    letter_list.append(char)
                if char.upper() in hidden_word.letters:
                    letter_list.append(char.upper())

    if not letter_list:
        letter_list = [letter]

    return letter_list


def print_game(points, the_word, guess_letters, hidden_word):
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
        print_the_word(hidden_word.what_letters(), hidden_word)
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
        print_the_word(guess_letters, hidden_word)
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


def print_the_word(guesses, hidden_word):
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
        if not key.isalnum():
            for i in hidden_word.letters[key]:
                the_word[i] = key

    print(' ' * 5, end='')

    for i in the_word:
        if i is None:
            print('__ ', end='')
        else:
            print(i, ' ', end='')

    print('\n')
    return the_word


def the_game(hidden_word):
    game_points = 0
    guess_letters = []

    print_the_word(guess_letters, hidden_word)

    while game_points < 6:

        new_letter = check_letter(input('\nIntroduce your letter guess: '), hidden_word)
        os.system('clear')

        for letter in new_letter:
            if letter.lower() in guess_letters:
                print('Hey, you already said this one! See?')
                continue

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

        the_word = print_the_word(guess_letters, hidden_word)
        print_game(game_points, the_word, guess_letters, hidden_word)


def get_hidden_word(lang):
    if lang == 'E':
        file = 'english_words.txt'
    else:
        file = 'spanish_words.txt'

    with open(file, "r") as word_list:
        words = word_list.read().split('\n')
    word = random.choice(words)
    return word


def initialize_the_game():
    game_option = input('Hey! It was about time to see you here!\nWhat modality of game \
do you want to play?\na) Player vs Player\nb) Player vs Machine\n--> ').lower()

    while True:
        if game_option == 'a':
            word = input('\nGreat! What is the word you want your friend to guess? --> ')
            break

        elif game_option == 'b':
            language = input('\nOk, then. What language do you want to use?\n\
- English (E)\n- Spanish (S)\n--> ').upper()
            while True:
                if language in ['E', 'S']:
                    word = get_hidden_word(language)
                    break
                else:
                    print('\nThis option is currently not available. We are working on \
it so you can have fun soon...')
            break

        else:
            game_option = input('Nop, you only have 2 options:\na) Player vs Player\n\
b) Player vs Machine\n\nSo choose wisely...\n--> ')

    os.system('clear')

    print('Let the game begin!\n\nWelcome, player!\nYou know how the HangMan works, right?\n\
Then go ahead and smash it!\n')
    return word


def main():
    hidden_word = Word(initialize_the_game())
    the_game(hidden_word)


main()
