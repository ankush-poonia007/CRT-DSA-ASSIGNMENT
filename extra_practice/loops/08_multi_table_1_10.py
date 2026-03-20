def multi_table(num):

    for i in range ( 1 , 11 ):
        print(f"{num} x {i} = {num*i}")


print ("Program to Print Multiple Table From 1 - 10 ")

for i in range ( 1 , 11 ):
    print("\n")
    print(f"Printing Table of {i} : ")
    print ("= x = x = x = x = x = x = x = x = x = x = x =")

    multi_table(i)
    print ("= x = x = x = x = x = x = x = x = x = x = x =")
    print("\n")
