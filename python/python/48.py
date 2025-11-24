

def fact_n(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)


fact_n(5)