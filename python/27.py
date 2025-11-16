list = (1,4,9,16,25,36,49,64,81,100)


number = int(input("ENTER THE NUMNER TO BE FOUND : "))
i = 0

while i < len(list):
    if(list[i] == number):
        print("NUMBER FOUNF :",number," AT THE INDEX : ",i)
    
    i += 1