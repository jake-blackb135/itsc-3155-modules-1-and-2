#Takes a user inputted string and prints out all the lower case letters then the upper case letters in the string

text = input("Enter a string: ")
capitals = ""
for x in text:
    if x == " ":
        continue
    elif not x.isupper():
        print(x, end = "")
    else:
        capitals += x

print("\n"+capitals)

