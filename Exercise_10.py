#Takes a user inputted string and prints each letter in the string 3 times

str = input("Enter a string\n")
list = []
for x in range(len(str)):
    for y in range(3):
        list.append(str[x])
    print(list, end = " ")
    list.clear()