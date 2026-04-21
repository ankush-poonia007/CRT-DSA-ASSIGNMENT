"""Write a program to check whether a number is Strong or not.
A number is Strong if sum of factorials of its digits equals the number.

Input:
Enter a number: 145

Output:
1! + 4! + 5! = 1 + 24 + 120 = 145
145 is a Strong Number
"""


def num_fact(num):
    if num <= 1:
        return 1
    return num_fact(num - 1) * num


def is_strong(num):
    total_sum = 0
    duplicate_num = num

    # Process each digit
    while num > 0:
        digit = num % 10
        total_sum += num_fact(digit)  # Add factorial to sum
        num //= 10  # Integer division to remove the last digit

    if total_sum == duplicate_num:
        print(f"{duplicate_num} is a Strong Number")
    else:
        print(f"{duplicate_num} is Not a Strong Number")


menu = ("Welcome to the program!!\n"
        "Ready to check your number for strong??\n"
        "Enter anything other than a number to Exit the program")

print("=" * 50)
print(menu)
print("=" * 50)

while True:
    try:
        number = int(input("Enter the Number to check: "))
        is_strong(number)
    except ValueError:
        print("You are exiting")
        print("Thank You!!")
        break
