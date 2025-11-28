#del key word

class student:
    def __init__(self, name):
        self.name = name


s1 = student("karan")
print(s1.name)
del s1.name

print(s1.name)
        