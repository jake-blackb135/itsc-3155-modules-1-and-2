#Takes an integer and outputs all squared values from 0 to the integer

num = int(input("Enter a number greater than 1\n"))

for x in range(num+1):
    print("The square of " + str(x) + " is " + str((x*x)))