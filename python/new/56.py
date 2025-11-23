f = open("mp.txt", "r")
 
line1 = f.readline(5) #it only reads lines by line at a time 5 means it wil read 5 char only
print(line1)
line2 = f.readline(2)
print(line2)
f.close()