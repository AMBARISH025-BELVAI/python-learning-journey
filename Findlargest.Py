num1 = int(input("enter number"))
num2 = int(input("enter number"))
num3  = int(input("enter number"))

if num1>num2 and num1>num3:
    print("largest:",num1)

elif num2>num1 and num2>num3:
    print("largest:",num2)

else:
    print("largest:", num3)
