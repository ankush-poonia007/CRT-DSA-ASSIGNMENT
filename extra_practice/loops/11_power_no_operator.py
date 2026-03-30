"""Write a program to calculate base^exponent
without using the ** operator or pow() function.

Input:
Enter the base: 2
Enter the exponent: 5

Output:
2 ^ 5 = 32"""

def power_no_operator ( base , exponent ):

    if exponent == 0 :
        return 1

    final = base

    for i in range ( 2 , exponent + 1  ) :
        final *= base

    return final

num = int(input("Enter the number : "))

power = int ( input ( "Enter the Exponent Power You want to get : "))

print ( power_no_operator( base = num , exponent= power))
