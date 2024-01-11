#Checks 2 user entered strings and determines if either string starts with the other.

firsttext = input("Enter a string\n")
secondtext = input("Enter a string\n")

if firsttext.startswith(secondtext):
    print("True")
elif secondtext.startswith(firsttext):
    print("True")
else:
    print("False")
