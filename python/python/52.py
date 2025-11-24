#fact using recurvece function


def fact(n = int(input("ENTER THE NUMBER : "))):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) * n
    
print(fact())