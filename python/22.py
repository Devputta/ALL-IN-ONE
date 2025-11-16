sub = {}
print(type(sub))
print(sub)

x = input("ENTER THE KANNADA MARKS : " )
sub.update({"KANNADA" : x})
y = input("ENTER THE ENGLISH MARKS : " )
sub.update({"ENGLISH" : y})
z = input("ENTER THE MATHS MARKS : " )
sub.update({"MATHS" : z})


print(len(sub))
print(sub)
