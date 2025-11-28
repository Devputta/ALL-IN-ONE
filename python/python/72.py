class students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self): #if u forget to put self then it showes the error because it need to take a method 
        print("Wellcome,",self.name) #self need to used when using object attribute
        print("Marks :",self.marks)
       
    
s1 = students("karan", 68) # in class object need to be used when class being called
s1.welcome() 



