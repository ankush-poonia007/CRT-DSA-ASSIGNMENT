smallest = float("inf")
largest = float("-inf")
while True:
    num = int ( input ("Enter the number :"))
    if smallest > num :
        smallest = num
    if largest < num:
        largest = num

    response = input ("Do you want to Continue y/n?")
    if response.lower() == "n" :
        break

print ( f"Smallest Numbers is : {smallest}\nLargest Number is : { largest }")
