class Combatant:
    # Combatant class generation that will have combatants information

    def __init__(self, name=None, initiative='Nothing', pg='Nothing'):
        # Combatant class object can be defined when called. Otherwise, system will ask:

        self.order = 0
        self.name = self.define_name(name)
        self.initiative = self.define_initiative(self.name, initiative)
        self.pg = self.define_pg(self.name, pg)

        self.combatant = [self.order, self.name, self.initiative, self.pg]

        print()

    def define_name(self, name):
        if name == None:
            return input('What is the name of this combatant? --> ')
        else:
            return name

    def define_initiative(self, name, initiative):
        return check_input(name, initiative, 'Initiative')

    def define_pg(self, name, pg):
        return check_input(name, pg, 'PG')




class Manager:
    # This class will be managing the game.

    def __init__(self):
        # combat container is generated:
        combat = []

        # Options for menu are generated:
        # self.options = {0: self.general_status, 1: self.attack,
        #                 2: self.delay_action, 3: self.add_status, 4: self.conduct_delayed_action,
        #                 5: self.add_combatant, 6: self.exit}

        self.initialize_combat(combat)
        self.arrange_combat(combat)

        print(combat)
        self.display_menu()

    def initialize_combat(self, combat):
        # Creates combatants and adds them to the combat container:

        Aiwe = Combatant('Aiwe', 'Vaya', 17)
        Klescknuk = Combatant('Klescknuk')
        # Mal = Combatant()

        self.add_combatant(Aiwe.combatant, combat)
        self.add_combatant(Klescknuk.combatant, combat)

    def add_combatant(self, combatant, combat):
        # This function adds a new combatant

        combat.append(combatant)

    def arrange_combat(self, combat):
        # This function is used to sort combatants as per initiative values.

        for i in combat:
            for j in combat:
                if i[2] == j[2] and i[1] != j[1]:
                    while True:
                        who = input('{} and {} have the same initiative value. Who should go first? --> '.format(
                            i[1],j[1]))
                        if i[1] == who:
                            i[2] += 0.01
                            break
                        elif j[1] == who:
                            j[2] += 0.01
                            break
                        else:
                            print('I am not asking about {}...\n'.format(who))

        combat.sort(key=lambda x: x[2],reverse=True)
        num = 0

        # After sorting combatants container, a sorting number is added to every combatant (first column):
        for i in combat:
            num += 1
            i[0] = num

    def display_menu(self):
        # Displays main menu:

        print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|   o---|==== Menu =====>   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| 0- General Status         |
|                           |
| 1- Attack                 |
| 2- Delay Action           |
| 3- Add Status             |
|                           |
| 4- Conduct Delayed Action |
| 5- Add Combatant          |
|                           |
| 6- Exit                   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

    # def run(self):
    #     while True:
    #         self.display_menu()
    #
    #         option = input('What will the option be? --> ')
    #
    #         valid_option = None
    #
    #         if option.isdecimal():
    #             option = int(option)
    #
    #             if option in self.options:
    #                 valid_option = True
    #
    #                 # Equivalent
    #                 self.options[option]()
    #
    #                 input('\n<enter>\n')
    #
    #             elif option == 6:
    #                 print('\nToday\'s combat is over, but the adventure hasn\'t finished yet...\n')
    #                 exit()
    #
    #         if not valid_option:
    #             print('I\'m sorry, you need to enter one of the options (number)')


def check_input(name, value, characteristic):
    # This check will be used specifically to check whether input is a number or not.
    # 'If' will be useful for initialization of combatants.

    if value == 'Nothing':
        value = input('What is {}\'s {} value? --> '.format(name, characteristic))

    # Common part for every check_input():
    while True:
        try:
            value = int(value)
        except ValueError:
            value = input('{} has to be a number. What is {}\'s initiative value? --> '.format(characteristic, name,
                                                                                               characteristic))

        if isinstance(value, int):
            break

    # Returns a value that is always an int:
    return value


if __name__ == '__main__':
    Manager()
