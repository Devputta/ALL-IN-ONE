# @staticmethod
#1. static method (nothing) -- (can't change in class or instance)

# @classmethod
#2. class method (cls) -- (only for class attribute make changes)

#3. instance method (self) -- (only used to make changes in instance variable)


class pu:

    def caolMarks(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem
        self.per = str((self.math + self.chem + self.phy) / 3 )+ "%"

    def cal(self):
        self.per = str((self.math + self.chem + self.phy) / 3 )+ "%"

p1 = pu()
p1.caolMarks(90,100,95)
print(p1.per)



p1.phy = 90
print(p1.phy)

p1.cal()
print(p1.per)
