"""Write a program to check whether a number is Automorphic or not.
A number is Automorphic if its square ends with the number itself.

Input:
Enter a number: 5

Output:
5² = 25 → ends with 5
5 is an Automorphic Number

---
Input:
Enter a number: 6

Output:
6² = 36 → ends with 6
6 is an Automorphic Number

---
Input:
Enter a number: 3

Output:
3² = 9 → does not end with 3
3 is not an Automorphic Number"""


menu = ("Welcome to the program!!\n"
        "Ready to check your number for strong??\n"
        "Enter anything other than a number to Exit the program")

print("=" * 50)
print(menu)
print("=" * 50)

while True:
    try:
        number = int(input("Enter the Number to check: "))
        is_Automorphic(number)
    except ValueError:
        print("You are exiting")
        print("Thank You!!")
        break
