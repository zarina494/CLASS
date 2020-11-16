class Planet:
    def __init__(self,name,position):
        self.name = name
        self.form = format
        self.position = position
        self.temp = 0
        self.size = 0
    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size)
class Mercury(Planet):
    def __init__(self,position,name = 'Mercury'):
        super().__init__(name,position)
        self.temp = 120
        self.size = 'small'
    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size)
class Jupyter(Planet):
    def __init__(self,position,name = 'Jupyter'):
        super().__init__(name,position)
        self.temp = 230
        self.size = 'bigger'
        self.briliant_rain = True
    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size,self.briliant_rain)
class Saturn(Planet):
    def __init__(self,position,name = 'Jupyter'):
        super().__init__(name,position)
        self.temp = -100
        self.size = 'middle'
        self.briliant_rain = True
        self.count_rings = 7
    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size,self.briliant_rain,self.count_rings)
jupyter = Jupyter('Solar sistem')
jupyter.description()
saturn = Saturn('Solar sistem')
saturn.description()



