
dict = { 0 : 0 , 1 : 0 , -1 : 0 }
while True:
    num = int ( input ("Enter the number :"))
    if num == 0 :
        dict [0] += 1
    elif num > 0 :
        dict [1] += 1
    else :
        dict [-1] += 1

    response = input ("Do you want to Continue y/n?")
    if response.lower() == "n" :
        break

print ( f"Postive Numbers {dict[1]}")
print ( f"Negative Numbers {dict[-1]}")
print (f"Zero Numbers {dict[0]}")