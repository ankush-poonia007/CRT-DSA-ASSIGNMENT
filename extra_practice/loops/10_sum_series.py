"""Write a program to find the sum of the series:
1 + 1/2 + 1/3 + 1/4 + ... + 1/n

Input:
Enter the value of n: 5

Output:
Sum of series = 2.2833"""


def sum_series(n):
    total = 0.0

    for i in range ( 1 , n + 1 ):
        total  += 1/i
    return round( total , 4 )

num = int(input("Enter the value of n: "))
result = sum_series(num)
print("Sum of series = ",result)