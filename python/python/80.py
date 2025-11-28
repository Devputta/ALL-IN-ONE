#inheritance is also one of the piller in opps concepte in python

#single inheritance

class car:
    color = "black"
    @staticmethod
    def started():
        print("The Car is started......")

    @staticmethod
    def stop():
        print("The Car is stoped!")

class tayota(car):
    def __init__(self,name):
        self.name = name

car1 = tayota("kia")

print(car1.name)