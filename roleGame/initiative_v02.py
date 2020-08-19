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
        return check_number(initiative, 'Initiative', name)

    def define_pg(self, name, pg):
        return check_number(pg, 'PG', name)




class Manager:
    # This class will be managing the game.

    def __init__(self):
        # combat container is generated:
        self.combat = []
        self.round = 0
        self.player_number = 0

        # Options for menu are generated:
        # self.options = {0: self.general_status, 1: self.attack,
        #                 2: self.delay_action, 3: self.add_status, 4: self.conduct_delayed_action,
        #                 5: self.add_combatant, 6: self.exit}

        self.initialize_combat()

        self.options = {0: self.general_status, 1: self.attack,
                        5: self.add_combatant}
        self.player = self.combat[self.player_number]

    def add_combatant(self, combatant):
        # This function adds a new combatant

        self.combat.append(combatant)
        self.arrange_combat()

    def arrange_combat(self):
        # This function is used to sort combatants as per initiative values.

        for i in self.combat:
            for j in self.combat:
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

        self.combat.sort(key=lambda x: x[2],reverse=True)
        num = 0

        # After sorting combatants container, a sorting number is added to every combatant (first column):
        for i in self.combat:
            num += 1
            i[0] = num

    def attack(self, attacker):
        # Attacker attacks to an individual in combat.
        # Following part identifies individual being attacked:

        while True:
            injured = check_name(input('Who is {} attacking to? (Enter to skip) --> '.format(
                attacker[1])), self.combat)

            if injured == '':
                break

            while True:
                if injured != 'No one':
                    break
                injured = check_name(input('This individual is not part of the combat. Who is {} attacking '
                                           'to? (\'No one\' to continue) --> '.format(attacker[1])), self.combat)



            # Following part checks damage and subtracts it from PGs:
            damage = check_number(input('How much damage does {} do? --> '.format(attacker[1])), 'Damage')
            self.combat[injured][3] -= damage

            print('{}\'s PG are now {}!!'.format(self.combat[injured][1], self.combat[injured][3]))

            # It also has into account if resulting PG are negative:
            if self.combat[injured][3] < 0:
                dead = 'Maybe'
                while True:
                    if dead.upper() == 'Y':
                        self.erase_combatant(injured)
                        print()
                        break
                    elif dead.upper() == 'N':
                        print()
                        break
                    else:
                        dead = input(
                            'Is {} dead with {} PG? (Y/N) --> '.format(self.combat[injured][1],
                                                                       self.combat[injured][3]))


    def display_menu(self):
        # Displays main menu:

        print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |   o---|==== Menu =====>   |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    | 0- General Status         | --> OK
    |                           |
    | 1- Attack                 | --> OK
    | 2- Delay Action           | --> Pending
    | 3- Add Status             | --> Pending
    |                           |
    | 4- Conduct Delayed Action | --> Pending
    | 5- Add Combatant          | --> OK
    |                           |
    | 6- End Player's round     | --> Ongoing
    | 7- Exit                   | --> OK
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    | Round --->""", self.round, end='')
        if self.round < 10:
            print(' '*13, '|', end='')
        elif self.round > 9:
            print(' ' * 12, '|', end='')
        else:
            print(' ' * 11, '|', end='')
        print("""
    | Player -->""", self.player[1], ' '*(13-len(self.player[1])),"""|
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    """)

    def erase_combatant(self, row):
        self.combat.remove(self.combat[row])
        print(self.combat)

    def initialize_combat(self):
        # Creates combatants and adds them to the combat container:

        Aiwe = Combatant('Aiwe', 'Nothing', 17)
        Klescknuk = Combatant('Klescknuk')
        # Mal = Combatant()

        self.add_combatant(Aiwe.combatant)
        self.add_combatant(Klescknuk.combatant)

    def general_status(self):

        print('~'*100)
        print(' '*40, 'ROUND', self.round)
        print('~' * 100)
        print('     Number', ' '*(25-7), 'Name', ' '*(25-5), 'Initiative', ' '*(25-11), 'PG', ' '*(25-3))
        print('~' * 100)
        for i in self.combat:
            if i == self.player:
                print(' --> ', end='')
            else:
                print('     ', end='')

            for j in i:
                print(j, ' '*(25-len(str(j))), end='')
            print()
        print('~' * 100)

    def run(self):
        while True:
            self.display_menu()

            option = input('What will the option be? --> ')

            valid_option = None

            if option.isdecimal():
                option = int(option)

                if option in self.options:
                    valid_option = True

                    self.options[option]()
                    input('\n<enter>\n')

                elif option == 6:
                    self.player_number += 1

                elif option == 7:
                    print('\nToday\'s combat is over, but the adventure hasn\'t finished yet...\n')
                    exit()

            if not valid_option:
                print('I\'m sorry, you need to enter one of the options (number)')


def check_name(name, matrix):

    if name == '':
        return ''

    i = 0
    while i < len(matrix):
        if matrix[i][1] == name:
            return i
        i += 1

    return 'No one'

def check_number(value, charact='Input', name=None):

    # This check will be used specifically to check whether input is a number or not.
    # 'If' will be useful for initialization of combatants.
    if value == 'Nothing' and name is not None:
        value = input('What is {}\'s {} value? --> '.format(name, charact))

    # Common part for every check_input():
    while True:
        try:
            value = int(value)
        except ValueError:
            if name == None:
                value = input('{} has to be a number... --> '.format(charact))
            else:
                value = input('{} has to be a number... What is {}\'s {}? --> '.format(charact, name, charact))

        if isinstance(value, int):
            break

    # Returns a value that is always an int:
    return value


if __name__ == '__main__':
    Manager().run()



