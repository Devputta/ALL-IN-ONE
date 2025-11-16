signal = input("ENTER THE SIGNALS LIKE 1>GREEN(GO), 2>YELLOW(READY), 3>RED(STOP) : ")

if(signal == "GREEN"):
    print("GO")
elif(signal == "RED" ):
    print("STOP!")
else:
    print("READY")