class Student:
    def __init__(self,name,laptop):
        self.name = name
        self.laptop = laptop
        self.height = 0
        self.sex = ''
    def __str__(self):
        return f'name:{self.name} laptop:{self.laptop} ' \
               f'height:{self.height} ' \
               f'sex:{self.sex}'
emir = Student('Emir','Lenovo')
emir.height = 170
emir.sex = 'male'
aijan = Student('Aijan','HP')
aijan.height = 170
aijan.sex = 'female'
print(emir,aijan)