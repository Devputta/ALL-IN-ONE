#super method

class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car has started..")

    @staticmethod
    def stop():
        print("Cars has stoped!")

class tayota(car):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name
        super().start()

c1 = tayota("KIA", "Eletrics")
print(c1.type)
