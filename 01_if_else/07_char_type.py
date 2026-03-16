ch = input("Enter the Values :")[0]

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("This is a Alphabet")
elif '0' <= ch <= '9':
    print("This is a Number")
else:
    print("This is a Special Character")