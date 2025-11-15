MARKS = int(input("ENTER THE MARKS : "))

if(MARKS >= 90):
    GRADE = "A"
elif(MARKS >= 80 and MARKS <=90):
    GRADE = "B"
elif(MARKS >=70 and MARKS <= 80):
    GRADE = "c"
else:
    GRADE = "D"

print("The Grade Is : ", GRADE)
