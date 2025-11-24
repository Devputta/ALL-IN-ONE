class Account():

    def __init__(self, balence, accno):
        self.balence = balence
        self.accno = accno
        print("You'r Balance was: ",self.balence,"/-")

    def debit(self,amount):
        self.balence -= amount
        print("Rs.",amount,"was depited from you'r Account no:",self.accno)
        
    def credit(self,amount):
        self.balence += amount
        print("Rs.",amount,"was Credited to you'r Account no:",self.accno)

    def bal(self):
        print("you'r Account no:",self.accno,"\nyou'r Balence is: Rs.",self.balence,"/-")
        

a1 = Account(10000,12345)
a1.debit(int(input("ENter the Debit amount :")))
a1.credit(100)
a1.bal()