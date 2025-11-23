f = open("mp.txt", "w+") # w+ means write with read
f.write("i am not blind")
print(f.read())
f.close()