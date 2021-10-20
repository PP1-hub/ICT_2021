n = int(input("Enter number of seconds: "))    #Units of Time (Again)

day = n // (24 * 3600)
 
n = n % (24 * 3600)
hour = n // 3600
 
n %= 3600
minutes = n // 60
 
n %= 60
seconds = n
     
print("The duration is:",day,":", hour, ":", minutes, ":",seconds)