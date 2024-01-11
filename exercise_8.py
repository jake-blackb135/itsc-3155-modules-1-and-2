list = []
for i in range(10):
    num = int(input("Enter an integer\n"))
    if num not in list:
        list.append(num)
print(list)