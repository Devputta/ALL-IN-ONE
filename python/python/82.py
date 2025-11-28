#multiple inheritance
class A:
    varA = "wellcome to my Class A"

class B:
    varB = " wellcome to my class B"

class C(A, B):
    varC = " wellcome to my class C"
    

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
