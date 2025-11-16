#palindrom

list = [4,3,4]

list_copy = list.copy()
list_copy.reverse()

if(list_copy == list):
    print("LIST IS PALINDEOM : ",list)
else:
    print("THE LIST IS NOT A PALINDROM :",list)