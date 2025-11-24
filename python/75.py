# oopps pillers
# 1.abstraction : it will hide implimentation part of the class and then it will only showes the essential features to the users
#EX:
class car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("CAR IS STARTED........")

c1 = car()
c1.start()

# 2. Encapsulation : wrapping data and function in to single unit(object)
# ex:
class students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self): 
        print("Wellcome,",self.name) 
        print("Marks :",self.marks)
       
    
s1 = students("karan", 68)
s1.welcome() 





