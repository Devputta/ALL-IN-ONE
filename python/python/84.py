class persion:
    name = "Rahul"

    def changeName(self, name):
        self.name = name

p1 = persion()
p1.changeName("mahadevu m p")
print(p1.name)  
print(persion.name)

#ex

class persion1:
    name = "Rahul"

    def changeName(self, name):
        persion1.name = name

p11 = persion1()
p11.changeName("mahadevu m p")
print(p11.name)  
print(persion1.name)
