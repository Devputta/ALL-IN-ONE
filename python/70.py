#constructer 

# init function is executed when object being called

class student:


    def __init__(self,fullname): #self is a reference to a current instance of the class used to access to the variable that belongs to the classes
        self.name = fullname
        print("Adding the students to the list")

s1 = student("maha")
print(s1.name)
s2 = student("raju")
print(s2.name)


