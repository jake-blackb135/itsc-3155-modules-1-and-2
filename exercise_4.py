nums = []
num = int(input("Enter a number\n"))

for x in range(num):
    nums.append(float(input("Enter number " + str(x) + ":")))

print(nums)
average = sum(nums)
average /= len(nums)
print("average: " + str(average))