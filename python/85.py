#class method decorator another way of changing class attrabute note static method can't acces or modify the class attrabute

class persion:
    name = "Rahum Kumar"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = persion()
p1.changeName("Ramesh Kumar")
print(p1.name)
print(persion.name)