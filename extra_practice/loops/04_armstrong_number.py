
def count_digits(num):
    if num == 0: return 1  # Fix: 0 has one digit
    num = abs(num)         # Fix: Handle negative inputs
    count = 0
    while num:
        num //= 10
        count += 1
    return count

def is_armstrong_number ( num ):
    if num < 0: return False

    digits = count_digits( num )
    digit_power_sum  = 0
    temp = num

    while num:
        digit = num % 10

        digit_power_sum  += digit**digits
        num //= 10

    return digit_power_sum  == temp
try :
    number = int(input("Enter a Number : "))

    if is_armstrong_number( number ):
        print ( f"{number} is a Armstrong Number")
    else:
        print ( f"{number} is not a Armstrong Number")
except ValueError:
    print ("Please enter a valid integer.")