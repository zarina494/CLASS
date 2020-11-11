class Design:
    def __init__(self,style,objects):
        self.style = style
        self.objects = objects
        self.furniture = 0
        self.place = 'place'

    def __str__(self):
        return (f'Stil kvartiry - {self.style}, Predmety neobhodimosti - {self.objects}, '
              f'Mebel - {self.furniture}, Mesto paspolojeniya kvartiry: {self.place}')
design = Design('Minimalizma','Tolko nujnie predmety')
design.furniture = 'VSE 4TO VY HOTELI'
design.place = 'Djal'
print(design)
