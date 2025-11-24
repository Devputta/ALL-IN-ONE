f = open("mp.txt", "r+") # r+ means read + write (over write at the begining of the file with ild char)
f.write("i am not blind")
print(f.read())
f.close()