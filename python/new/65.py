with open("practice.txt", "r") as f:
    data = f.read()

new = data.replace("java", "Python") # string replace method is used
print(new)

with open("practice.txt", "w") as f:
    f.write(new)