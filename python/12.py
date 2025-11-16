#GRATEST OF 4 NUMBER

num1 = int(input("ENTER THE 1st NUMBER : "))
num2 = int(input("ENTER THE 2nd NUMBER : "))
num3 = int(input("ENTER THE 3rd NUMBER : "))
num4 = int(input("ENTER THE 4th NUMBER : "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4 ):
    print("1st NUMBER IS GRATER : ",num1)
elif(num2 >= num3 and num2 >= num4):
    print("2nd NUMBER IS GRATER : ",num2)
elif(num3 >= num4):
    print("3rd NUMBER IS GRATEST : ",num3)
else:
    print("4rd NUMBER IS GRATER : ",num4)