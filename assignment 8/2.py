n = int(input("Enter number:"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of numbers is: ", sum)
avg = sum / n
print("Average of numbers is", avg)