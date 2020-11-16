class Phone:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.memory = 32
        self.price = 200
        self.battery = 0
        self.touchid = 5
        self.locked = False
    def description(self):
        print(self.name,self.model,self.year,self.memory,self.price,self.battery,
              self.touchid,self.locked)
    def set_battery(self,charge):
        if not self.locked:
            if 0<charge<=100:
                self.batery = charge
            else:
                print('Obratites v salon!')
    def unlock(self,tries):
        if 0<tries<self.touchid:
            print('Vy zashli!')
        else:
            self.locked = True
            print('Poprobuite cherez 30 sekund!')
iphone = Phone('Iphone','12pro','2019')
iphone.price = 110
iphone.unlock(6)
iphone.set_battery(100)
iphone.description()