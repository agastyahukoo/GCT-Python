ch = input("Enter a character: ")
ch = int(ord(ch))
if (ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122):
    print("The character is a letter.")
elif (ch >= 48 and ch <= 57):
    print("The character is a digit.")
else:
    print("The character is a special character.")