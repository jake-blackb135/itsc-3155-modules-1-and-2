#Creates three empty arrays and fills the first 2 with user inputted integers

list1 = []
list2 = []
list3 = []
list1.append(int(input("Enter a number for the first list: \n")))
list1.append(int(input("Enter a number for the first list: \n")))
list1.append(int(input("Enter a number for the first list: \n")))
list1.append(int(input("Enter a number for the first list: \n")))
list1.append(int(input("Enter a number for the first list: \n")))

list2.append(int(input("Enter a number for the second list: \n")))
list2.append(int(input("Enter a number for the second list: \n")))
list2.append(int(input("Enter a number for the second list: \n")))
list2.append(int(input("Enter a number for the second list: \n")))
list2.append(int(input("Enter a number for the second list: \n")))


#Goes through the arrays and adds every value that appears in both arrays to list 3, then prints the resulting array.
for x in range(len(list1)):
    if list1.count(list2[x]):
        if list3.count(list2[x]):
            continue
        else:
            list3.append(list2[x])
print(list3)
