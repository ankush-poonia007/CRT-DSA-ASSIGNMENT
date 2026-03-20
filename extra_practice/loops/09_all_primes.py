import math
def is_prime( num ):
    isprime = True
    for i in range ( 2, int ( math.sqrt(num)) +1  ):

        if num % i == 0 :
            return False
            break
    return True

number = int ( input ( "Enter the Number : "))
print ( f"Program to check prime Number form 1- {number} ")

for i in range (2 , number+1 ):

    if is_prime( i ):
        print( f"Number {i} is a Prime Number ")
    else:
        print( f"Number {i} is Not a Prime Number ")