def natural(n):
    if(n == 0 ):
        return 0
    return natural(n-1) + n


a = natural(5)
print(a)