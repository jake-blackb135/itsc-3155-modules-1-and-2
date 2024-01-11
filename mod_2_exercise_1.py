#Takes a user inputted string and prints it out in reverse

text = input("Enter a string: ")
for x in reversed(text):
    print(x, end = "")

