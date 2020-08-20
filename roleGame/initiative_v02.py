class Combatant:
    # Combatant class generation that will have combatants information

    def __init__(self, name=None, initiative='Nothing', pg='Nothing'):
        # Combatant class object can be defined when called. Otherwise, system will ask:

        self.order = 0
        self.name = self.define_name(name)
        self.initiative = self.define_initiative(self.name, initiative)
        self.pg = self.define_pg(self.name, pg)
        self.status = ['-']

        self.combatant = [self.order, self.name, self.initiative, self.pg, self.status]

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

        self.initialize_combat()

        self.options = {0: self.general_status, 1: self.start_combat, 2: self.attack, 3: self.delay_action,
                        4: self.add_status, 5: self.conduct_delayed_action,
                        6: self.add_combatant, 7: self.next_combatant}

        self.define_player()

    def add_combatant(self, combatant=None):
        # This function adds a new combatant
        while True:
            if combatant is None:
                name = input('What will be the name of this new combatant? (Enter to skip) --> ')
                if name != '':
                    combatant = Combatant(name)
                    combatant = combatant.combatant
                else:
                    break

            self.combat.append(combatant)
            self.arrange_combat()
            break

    def add_status(self):
        player = self.bucle('What player are you adding a status upon? (Enter to skip) --> ',
                       'This individual is not part of the combat. What player are you adding a status'
                       ' upon? (Enter to skip) --> ')

        if player != '':
            status = input('What status are you adding upon {}? (Enter to skip) --> '.format(self.combat[player][1]))
            rounds = check_number(input('How many rounds will it last? --> '), status)

            if status != '':
                if self.combat[player][4] == ['-']:
                    self.combat[player][4] = [[status, rounds]]
                else:
                    self.combat[player][4].append([status, rounds])

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

    def attack(self):
        # Attacker attacks to an individual in combat.
        # Following part identifies individual being attacked:

        attacker = self.player

        injured = self.bucle('Who is {} attacking to? (Enter to skip) --> '.format(attacker[1]),
              'This individual is not part of the combat. Who is {} attacking to? (Enter to skip) '
              '--> '.format(attacker[1]))

        if injured != '':
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
                        break
                    elif dead.upper() == 'N':
                        break
                    else:
                        dead = input(
                            'Is {} dead with {} PG? (Y/N) --> '.format(self.combat[injured][1],
                                                                       self.combat[injured][3]))

    def bucle(self, sentence_1, sentence_2):

        player = check_name(input(sentence_1), self.combat)

        while True:
            if player != 'No one':
                break
            player = check_name(input(sentence_2), self.combat)

            if player == '':
                break


        return player

    def conduct_delayed_action(self):

        conducter = self.bucle('Who does conduct its action? (Enter to skip) --> ',
                   'This individual is not part of the combat. Who is conducting its action? (Enter to skip) --> ')

        self.combat[conducter][2] = self.player[2] + 0.01
        self.player = self.combat[conducter]
        self.arrange_combat()

    def define_player(self):
        # Defines player based on self.player_number.
        self.player = self.combat[self.player_number]

    def delay_action(self):
        # Basically skips player.
        if self.player[4] == ['-']:
            self.player[4] = ['Action delayed']
        else:
            if 'Action delayed' not in self.player[4]:
                self.player[4].append('Action delayed')

        self.next_combatant()

    def display_menu(self):
        # Displays main menu:

        print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |   o---|==== Menu =====>   |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    | 0- General Status         |
    | 1- Start Combat           |
    |                           |
    | 2- Attack                 |
    | 3- Delay Action           |
    | 4- Add Status             |
    |                           |
    | 5- Conduct Delayed Action |
    | 6- Add Combatant          |
    |                           |
    | 7- End Player's round     |
    | 8- Exit                   |
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

    def general_status(self):

        print('~'*140)
        print(' '*40, 'ROUND', self.round)
        print('~' * 140)
        print('     Number', ' '*(17-len('Number')), 'Name', ' '*(17-len('Name')), 'Initiative',
              ' '*(18-len('Inititative')), 'PG', ' '*(17-len('PG')), 'Status')
        print('~' * 140)
        for i in self.combat:
            if i == self.player:
                print(' --> ', end='')

                for k in i[4]:
                    if k == 'Action delayed':
                        i[4].remove(k)
                if i[4] == []:
                    i[4] = ['-']
            else:
                print('     ', end='')

            for j in i:
                if isinstance(j, list) == True:
                    for k in j:
                        if isinstance(k, list) == True:
                            for l in k:
                                print(l, '', end='')
                        else:
                            print(k, end='')
                        if k != j[-1]:
                            print(' / ', end='')

                else:
                    print(j, ' '*(18-len(str(j))), end='')
            print()
        print('~' * 140)

    def initialize_combat(self):
        # Creates combatants and adds them to the combat container:

        Aiwe = Combatant('Aiwe', 15, 17)
        Klescknuk = Combatant('Klescknuk', 20, 13)
        Mal = Combatant('Mal', 12, 15)

        self.add_combatant(Aiwe.combatant)
        self.add_combatant(Klescknuk.combatant)
        self.add_combatant(Mal.combatant)

    def next_combatant(self):
        # Defines next combatant and, if applicable, next round.
        self.player_number += 1

        if self.player_number > len(self.combat) - 1:
            self.player_number = 0
            self.next_round()

        self.define_player()
        print('Now it is {}\'s round!'.format(self.player[1]))

        for i in self.player[4]:
            counter_0 = 0

            if isinstance(i, list):
                counter_1 = 0
                for j in i:
                    if isinstance(j, int) == True:
                        self.player[4][counter_0][counter_1] -= 1
                        if self.player[4][counter_0][counter_1] == 0:
                            self.player[4].remove(i)
                    counter_1 += 1

            counter_0 +=1

    def next_round(self):
        self.round += 1

    def run(self):
        # This will run the game.
        # There are two ways of measuring time and they go in parallel:
        # 1 - self.round --> Global combat round
        # 2 - self.player_number --> Who is playing inside the current round

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

                elif option == 8:
                    print('\nToday\'s combat is over, but the adventure hasn\'t finished yet...\n')
                    exit()

            if not valid_option:
                print('I\'m sorry, you need to enter one of the options (number)')

    def start_combat(self):
        self.round = 1
        self.player = self.combat[0]


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



