def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data): # find is aswell as string method 
            print("Found")
        else:
            print("not Found")

# check_for_word()

def check_for_line():
    word = "learning"
    line = 1
    data = True
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("found in line no: ",line)
                return
            line += 1
    return -1

print(check_for_line())