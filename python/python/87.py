#property decorator

class pu:

    def calMarks(self, m, c, p):
        self.m = m
        self.c = c
        self.p = p

    @property
    def Persentage(self):
        return str((self.m + self.p + self.c) /3) + "%"
    
p1= pu()
p1.calMarks(100, 80, 90)
print(p1.Persentage)

p1.p = 100
print(p1.Persentage)


