#Creates a table made from 0s and places a value of 1 at the coordinates the user specifies

row = int(input("enter a row num from 1-5: \n"))
col = int(input("enter a col num from 1-5: \n"))
for x in range(5):
    for y in range(5):
        if x == row -1 and y == col -1:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print(" ")