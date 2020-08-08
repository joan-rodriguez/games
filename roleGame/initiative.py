class Combatant:
    def __init__(self):

        self.name = input('What is the combatant name? ')
        self.initiative = int(input('What is its initiative? '))
        self.pg = int(input('What is its PG? '))

        self.array = {'Name': self.name, 'Init': self.initiative, 'PG': self.pg}


class Manager:
    def __init__(self):

        self.combat = []
        self.order()

    def attack(self, name, damage):
        for p in self.combat:
            if p['Name'] == name:
                p['PG'] = p['PG'] - damage

                print()
                print('----->  Now {} has {} PG!!'.format(p['Name'], p['PG']))
                print()

                if p['PG'] < 0:
                    if self.check_death(p['PG']) is True:
                        self.combat.remove(p)

    def check_death(self, pg):
        dead = input('Is this combatant with {} dead? [Enter to skip] '.format(pg))
        if dead.lower() == 'y':
            print()
            return True

    def check_attacked(self, name):
        for p in self.combat:
            if p['Name'] == name:
                return True

    def order(self):

        while True:
            combatant = Combatant()
            self.combat.append(combatant.array)

            more = input('\n Are there more combatants? (Y/N) ')
            print()
            if more.lower() == 'n' or more == '':
                break

        self.combat.sort(key=lambda x: x.get('Init'), reverse=True)

    def print_turno(self, turno):
        print('~~~~~~~~~~~~~~~~~~~~~~\n--ROUND #{}--\n~~~~~~~~~~~~~~~~~~~~~~'.format(turno))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for p in self.combat:
            print(p)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()

    def run(self):
        turno = 0

        while True:
            turno += 1
            self.print_turno(turno)

            for i in self.combat:
                print('{} -- {}PG\n------------------------------'.format(i['Name'], i['PG']))
                attacked = input('Does it attack? If so, to whom? [Enter to skip] ')

                while True:
                    while True:
                        if self.check_attacked(attacked) is True:
                            break

                        if attacked == '':
                            print()
                            break

                        attacked = input('This individual does not exist (anymore?). Now, does it attack? '
                                         'If so, to whom? [Enter to skip] ')

                    if attacked == '':
                        print()
                        break

                    damage = int(input('How much damage does it make? '))
                    self.attack(attacked, damage)
                    attacked = input('Does it attack again? If so, to whom? [Enter to skip] ')


if __name__ == '__main__':
    Manager().run()
