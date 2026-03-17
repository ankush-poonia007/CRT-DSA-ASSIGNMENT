import math

num = int ( input ("Enter the number "))
isprime = True
for i in range ( 2,(round(math.sqrt(num))+1)):

    if num % i == 0 :
        isprime = False
        print ( f"{num} is not a Prime Number")
        break
if isprime:
    print(f"{num} is a Prime Number")