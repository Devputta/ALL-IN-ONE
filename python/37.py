i = 0
while i <= 10:
    if( i % 2 == 0):
        i += 1
        continue # skip
    print(i)
    i += 1


for i in range(1,100,2):
    print(i)