#Creates an empty array and adds all even numbers the user inputs into the array until the user quits, then prints the array

list = []
inp = input("Enter a number or QUIT to quit: ")
if int(inp) % 2 == 0:
    list.append(int(inp))
while inp != "QUIT":
    inp = input("Enter a number or QUIT to quit: ")
    if inp == "QUIT":
        continue
    elif int(inp) % 2 == 0:
            list.append(int(inp))
        
    else:
        continue
print(list)
