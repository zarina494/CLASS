class Game:
    def __init__(self,player):
        self.player = player
        self.ships = 4
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0
        self.position4 = 0
    def player_attack(self,attack_position):
        if self.position1 == attack_position or self.position2 == attack_position or self.position3 ==attack_position or self.position4 == attack_position:
            print('Popal! Vybirai novuyu cel!')
            self.ships = self.ships - 1
        else:
            print('Poterya hoda')
class Lions(Game):
    def __init__(self,player,position1,position2,position3,position4):
        super().__init__(player)
        self.position1 = position1
        self.position2 = position2
        self.position3 = position3
        self.position4 = position4
class Tigers(Game):
    def __init__(self,player,position1,position2,position3,position4):
        super().__init__(player)
        self.position1 = position1
        self.position2 = position2
        self.position3 = position3
        self.position4 = position4
lion1 = Lions('Simba', 10,11,12,13)
tiger1 = Tigers('Diego',6,7,8,9)

tiger1.player_attack(6)
tiger1.player_attack(12)
lion1.player_attack(11)
lion1.player_attack(12)
print(tiger1.ships,lion1.ships)



