class Person:
    def __init__(self, name, sex, race, role):
        self.name = name
        self.sex = sex
        self.race = race
        self.role = role
        self.position = 0
        self.health = 100
        self.damage = 10
        self.armor = 5
        self.level = 0

    def move(self, new_position):
        if new_position > 0:
            self.position = new_position
        else:
            print('Переместите в правильное место!')

    def experience(self, xp):
        exp_list = [200, 600, 1800, 5400, 20000]
        for exp in exp_list:
            if xp > exp:
                self.level += 1
                xp -= exp
                self.health += 100
                self.damage += 2
                self.armor += 5

    def death(self):
        if self.health <= 0:
            print('You Died!')

    def plate(self, item):
        if item == 'common':
            self.health += 30
            self.armor += 5
        elif item == 'legendary'and self.level < 4:
            self.health += 2000
            self.armor += 300

    def sword(self,item):
        if item == 'common':
            self.damage = self.damage + 10
        elif item == 'legendary' and self.level < 4:
            self.damage = self.damage + 1000

    def description(self):
        print(self.name, self.race, self.sex, self.role, self.position, self.damage, self.armor, self.level, self.health)

class Warrior(Person):
    def __init__(self, name, sex, race, role = 'Warrior'):
        super().__init__(name, sex, race, role)
        self.position = 20
        self.health = 500
        self.armor = 20
        self.damage = 25






class Fight:
    def __init__(self,health,damage):
        self.health = health
        self.damage = damage


    def __add__(self, other):
        result = self.health - self.damage
        return result

warrior1 = Warrior('Hector', 'male', 'human')
warrior2= Warrior('Ali','m','human')
warrior1.damage = 50
fight1 = Fight(warrior1.health,warrior2.damage)
fight2 = Fight(warrior2.health,warrior2.damage)
result1,result2 = 1,1
while result1 > 0 and result2 > 0:
    result1 = fight1 + fight2
    result2 = fight2 + fight1
    fight1 = Fight(result1,warrior1.damage)
    fight2 = Fight(result2, warrior2.damage)
if result1 > 0:
    print(f'Pobedil: {warrior1.name}')
else:
    print(f' Pobedil: {warrior2.name}')



    print(result1,result2)


