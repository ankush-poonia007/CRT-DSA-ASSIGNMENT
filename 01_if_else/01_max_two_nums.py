# input() reads as string, so we cast to int
num1 = int(input("Enter the Number1 : "))
num2 = int(input("Enter the Number2 : "))

if num1 > num2:
    print(f"Maximum Number is {num1}")
elif num2 > num1:
    print(f"Maximum Number is {num2}")
else:
    print("Both numbers are equal.")