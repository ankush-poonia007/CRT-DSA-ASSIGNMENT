num = int(input("Enter the Number : "))

# The % operator finds the remainder
if num % 5 == 0 and num % 11 == 0:
    print("This Number is Divisible by 5 and 11")
else:
    print("This Number is Not Divisible by 5 and 11")