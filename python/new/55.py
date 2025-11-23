#file io in python 

f = open("mp.txt", "r") # r is default 

data = f.read() # entire file
print(data)
print(type(data))
f.close()