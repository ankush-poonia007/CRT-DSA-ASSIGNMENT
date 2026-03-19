def is_palindrome( num ):

    # Negative numbers and numbers ending in 0 (except 0 itself) aren't palindromes
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    
    rev = 0
    temp = num
    while temp > 0:
        # Standard digit reversal logic
        rev = (rev * 10) + (temp % 10)
        temp //= 10

    return rev == num


number = int ( input ("Enter a number to Check for Palindrome: "))
response = is_palindrome( number )

print (f"{number} is a Plindrome" if response else f"{number} is not a Palindrome")