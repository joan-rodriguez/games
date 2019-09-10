""" Hangman, the game"""
import random


class Word:
    def __init__(self, name, length, letters):
        self.name = name
        self.length = len(name)
        self.letters = what_letters(name)

    def what_letters(self):
        letters = {}
        position = 0
        for letter in self.name:
            if letter in letters:
                letters[letter] = position
            letters[letter][self.name.count(letter)]
        position += 1
        return letters

'''
Importar:
- random
- llistes de paraules

Classe:
- Paraula - atributs: número de lletres

Funcions:
- "Manager" - Joc
- Triar idioma i paraula
- Comptador
- Dibuixar hangman
- '''