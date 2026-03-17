#18.	Write a program to print reverse tables

num = int ( input ( "Enter the number: "))

print( f"Table of number {num}")

for i in range ( 10 , 0,-1 ):
    print(f"{num} * {i} = {num * i }")