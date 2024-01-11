# Creates an array with the length provided by user input

nums = []
num = int(input("Enter a number\n"))

# loops through the length of the array fills it with user provided numbers
for x in range(num):
    nums.append(float(input("Enter number " + str(x) + ":")))


# Prints the array and the average of all numbers in the array
print(nums)
average = sum(nums)
average /= len(nums)
print("average: " + str(average))