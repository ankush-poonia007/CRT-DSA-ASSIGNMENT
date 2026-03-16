ch = input("Enter the Character :")[0]

if 'a' <= ch <= 'z':
    print("This is a Small Alphabet")
elif 'A' <= ch <= 'Z':
    # Note: Corrected from your Java file which labeled this as 'Number'
    print("This is a Uppercase Alphabet")
else:
    print("This is Not an Alphabet")