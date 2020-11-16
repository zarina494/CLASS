class Book:
    def __init__(self,type, name):
        self.name = name
        self.type = type
        self.days = 5
        self.days = 6
        self.pisatel = 0
    def borrow_book(self,day):
        self.days =day and self.days=day

class Clssika(Book):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.type_literatury = 'Dlya roditeley'
        self.pisatel = 'Gipperreiter'
    def description(self):
        print(f'Kniga-{self.name}, {self.type}, Auditoriya-{self.type_literatury}, Avtor-{self.pisatel}')
kniga = Clssika('Deti','Klassika')
kniga.description()