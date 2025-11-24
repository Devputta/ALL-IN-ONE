#recursive function

def num(n = int(input("ENTER THE NUMBER : "))):
    if(n == 0):  #base case it will deside condition shoud go or not
        return
    print(n)
    num(n-1)

num()