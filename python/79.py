# private are defind like "__"  this means private attribute and methods ment tobe used within the class not at the out side the class 

class student:
    __name = "Rajath"

    def __hello(self):
        print("Hi Hello")
        print(self.__name)

    def wellcome(self):
        self.__hello()
        print(self.__name)

s1 = student()
print(s1.wellcome())