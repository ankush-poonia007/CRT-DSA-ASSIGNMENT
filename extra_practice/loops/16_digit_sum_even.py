"""Write a program to print all numbers between 1 to n
whose sum of digits is even.

Input:
Enter the limit: 20

Output:
Numbers with even digit sum:
2 4 6 8 11 13 15 17 20
"""

menu = ("Welcome to the program!!\n\n"
        "Enter anything other than a number to Exit the program")


print("="*50)
print(menu)
print("="*50)
def check_for_even(num) ->bool:

    sum = 0

    while num>0 :
        digit = num%10
        sum += digit
        num//=10

    return sum%2==0

def even_sum_digit( num ):

    if num <= 1 :
        return -1
    for i in range ( 2 , num+1 ):

        if check_for_even( i ):
            print( i , end=" ")
    print("")

while True:
    try:
        number = int(input("Enter the Number to check: "))
        even_sum_digit(number)
    except ValueError:
        print("You are exiting")
        print("Thank You!!")
        break