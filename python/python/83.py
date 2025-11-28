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
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        super().stop()

c1 = tayota("KIA", "Eletrics")
print(c1.type)
