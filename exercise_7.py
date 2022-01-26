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
