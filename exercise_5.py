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

for x in range(len(list1)):
    if list1.count(list2[x]):
        if list3.count(list2[x]):
            continue
        else:
            list3.append(list2[x])
print(list3)
