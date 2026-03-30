"""Write a program to check whether a given number is a Neon number or not.
A number is Neon if the sum of digits of its square equals the number itself.

Input:
Enter a number: 9

Output:
9 is a Neon Number

---

Input:
Enter a number: 8

Output:
8² = 64 → 6 + 4 = 10 ≠ 8
8 is not a Neon Number"""

def neon_number ( num ):

    final = pow( num , 2 )

    sum_ = 0
    while final :
        sum_ += (final % 10 )
        final = final // 10
    return sum_ == num

number = int ( input ( "Enter the number you want to check for neon number : "))

if neon_number( number ) :
    print( f"{number } is a Neon Number ")
else:
    print(f"{number } is not a Neon Number ")

