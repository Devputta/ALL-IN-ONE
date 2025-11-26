# private in python

class Account:
    def __init__(self,accno,accpass):
        self.accno = accno
        self.__accpass = accpass

    def priv(self):
        print(self.__accpass)

a1 = Account(12345, "ab1234cd")
print(a1.accno)
# print(a1.__accpass)
print(a1.priv())
