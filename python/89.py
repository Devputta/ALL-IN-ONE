#using dunder gunction (__add__)

class complexxx:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def complec(self):
        print(self.real,"i +", self.img,"j")

    def add(self, c2):
        realNew = self.real + c2.real
        imgNew = self.img + c2.img
        return complexxx(realNew, imgNew)

c1 = complexxx( 2, 6)
c1.complec()

c2 = complexxx(4, 2)
c2.complec()

c3 = c1.add(c2)
c3.complec()