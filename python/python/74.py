#static metod in python it will never take self as parametor so but it need to have decorator

class simple:
 
    @staticmethod # method Convert a function to be a static method.
    def sim():
        print("Wellcome to static metods..........")

s1 = simple()
s1.sim()