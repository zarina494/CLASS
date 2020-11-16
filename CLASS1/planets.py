class Planet:
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color
        self.temp = -150
        self.oxygen = False
        self.water = False
        self.humanity = False
    def description(self):
        print(f'Nazvanie planety - {self.name}, Razmer - {self.size}, svet - {self.color},'
              f'temperatura - {self.temp}.'
              f'Nalichie vozduha - {self.oxygen}, voda - {self.water} Chelovechestv -{self.humanity}')
    def set_humanity(self):
        self.humanity = True
        self.oxygen = True
        self.water =  True
        self.temp = 15
    def population(self,people):
        if self.humanity and self.water and self.oxygen:
            if people > 0:
                self.humanity = people
            else:
                print('Ne baluisya')
        else:
            print('Jizni net!')




earth = Planet('Earth', 20,'blue')
earth.set_humanity()
earth.population(2)



earth.description()  # metot vyzova on pokazyvart



