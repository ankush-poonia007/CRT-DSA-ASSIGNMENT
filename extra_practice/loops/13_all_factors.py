"""Write a program to print all factors of a number.

Input:
Enter a number: 12

Output:
Factors of 12 are: 1 2 3 4 6 12
"""


def factors ( num ):

    arr = []
    for i in range ( 1 , num + 1 ):
        if num % i == 0 :
            arr.append ( i )
    print(f"Factors of {num} are :",end=" ")
    for ele in arr :
        print(ele,end=" ")
    print("")

menu = "Enter a number to find all the Factors and enter anything other than a number to exit "
#Test Cases:
print("==========================================================================================")
print(menu)
print("==========================================================================================")

while True:

    try :
        num = int(input("Enter a number: "))

        factors(num)

    except ValueError :
        print("You chose to exit\nThank You!!")
        break

