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
    def __init__(self, brand, type):
        self.type = type
        super().started()
        super().stop()
        super().__init__(brand)


car1 = fortuner("b1","diesel")



print(car1.brand)