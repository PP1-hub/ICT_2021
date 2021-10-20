days = int(input("Enter number of Days: ")) * 3600 *24    #Units of Time
hours = int(input("Enter number of Hours ")) *3600
minutes = int(input("Enter number of Minutes: ")) *60
seconds = int(input("Enter number of Seconds: "))

total = days + hours + minutes + seconds
print("Total number of seconds:", total)