"""El Tres is a cards game. You already know the rules."""


class Card:
    """Represents a card. It will be defined by number and type."""

    def __init__(self, card_number, card_type):
        self.number = card_number
        self.type = card_type


class Deck:
    """Represent the deck of cards. Tipically will have 54 cards (13*4 + 2)."""

    def __init__(self, high_number=13, type_total=4, jokers=2):
        self.high_number = high_number
        self.type_total = type_total
        self.jokers = jokers

        self.deck_total = self.high_number * self.type_total + self.jokers


class Discard:
    """Represent all discarded cards."""

    def __init__(self):
        self.cards = []


class Player:
    """Represent a player."""

    def __init__(self, player_name, player_order):
        self.name = player_name
        self.order = player_order


class Hand:
    """Represents the hand of a player. It will have cards inventory."""

    def __init__(self, player_name):
        self.name = player_name


# class Menu:
#    """Display menu and respond to choices when run."""
