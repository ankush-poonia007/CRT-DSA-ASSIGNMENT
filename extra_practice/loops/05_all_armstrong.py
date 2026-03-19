
def count_digits(num):
    if num == 0: return 1  # Fix: 0 has one digit
    num = abs(num)         # Fix: Handle negative inputs
    count = 0
    while num:
        num //= 10
        count += 1
    return count

def is_armstrong_number ( num ):

    digits = count_digits( num )
    new_num = 0
    temp = num

    while num:
        digit = num % 10

        new_num += digit**digits
        num //= 10

    return new_num == temp


count = 0
for i in range(1, 501):
    if is_armstrong_number( i ):
        print ( f"{i} is a Armstrong Number = = = = = = = = = = ")
        count += 1
    else:
        print ( f"{i} is not a Armstrong Number")

print ( f"Total Number of Armstrong Number in range 1-500 : {count}")