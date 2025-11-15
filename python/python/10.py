#GRATEST OF 3 NUMBER

num1 = int(input("ENTER THE 1st NUMBER : "))
num2 = int(input("ENTER THE 2nd NUMBER : "))
num3 = int(input("ENTER THE 3rd NUMBER : "))

if(num1 > num2 and num1 > num3):
    print("1st NUMBER IS GRATER : ",num1)
elif(num2 > num3):
    print("2nd NUMBER IS GRATER : ",num2)
else:
    print("3rd NUMBER IS GRATER : ",num3)