list = [1, 4, 6, 16,25 ,36,49,64, 81,100,49]

for i in list:
    print(i)

x = 49
n = 0
for i in list:
    if(i == x):
        print("THE X IS FOUND", x, "at index: ",n)
        break
    n += 1
    