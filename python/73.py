#non static methods mean which are using self in metod or constructure in programing

class students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("THE student name with marks :..")

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        avg = sum/len(self.marks)
        print("THE NAME :",self.name, "\nMarks :",self.marks, "\nTotal Marks :",sum, "\nAVG :",avg)

s1 = students("Raj" ,[40,50,60,100])
s1.avg()





    