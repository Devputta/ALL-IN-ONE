sri1 = "I am a Software Engineer From Malavalli"
print(sri1.endswith("lli"))                              # string end with function 
print(sri1.endswith("MP"))

print(sri1.capitalize())                               # capitalizeing 1st char

print(sri1.replace("a","o"))                           #replace it will replace old with new

print(sri1.find("o"))                                    # find finction return index of the perticular word

print(sri1.count("a"))                                  # times of occurence char and word as well


name = input("ENTER THE NAME : ")
LEGN = len(name)
print("NAME = ",name,"||", "THE LENGTH OF NAME IS : ",LEGN,"||",  "THE $ OCCURENCE IS: ", name.count("$"))