#17.	Write a program to print tables

num = int ( input ( "Enter the number: "))

print( f"Table of number {num}")

for i in range ( 1 , 11 ):
    print(f"{num} * {i} = {num * i }")