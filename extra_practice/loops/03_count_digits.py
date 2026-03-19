def count_digits(num):
    if num == 0: return 1  # Fix: 0 has one digit
    num = abs(num)         # Fix: Handle negative inputs
    count = 0
    while num:
        num //= 10
        count += 1
    return count

num = int ( input ( "Enter the a Number: "))
digits = count_digits(num)
print ( f"The number {num} have {digits} digits" )