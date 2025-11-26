#inheritance is also one of the piller in opps concepte in python

#multi level inheritance

class car:
    
    @staticmethod
    def started():
        print("The Car is started......")

    @staticmethod
    def stop():
        print("The Car is stoped!")

class tayota(car):
    def __init__(self,brand):
        self.brand = brand

class fortuner(tayota):
    def __init__(self, type):
        self.type = type


car1 = fortuner("diesel")
car1 = tayota("b1")

car1.started()
print(car1.brand)