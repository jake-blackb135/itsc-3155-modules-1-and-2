text = input("Enter a string: ")
capitals = ""
for x in text:
    if x == " ":
        continue
    elif not x.isupper():
        print(x, end = "")
    else:
        capitals += x
    
print(capitals)

