#with is a built in type in python in this there is no need to close the file it will automaticlly it will close it

with open("mp.txt","r") as f:
    data = f.read()
    print(data)