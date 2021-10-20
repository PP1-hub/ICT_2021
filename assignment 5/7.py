temperature = int(input("Enter the air temperature in (degrees Celsius): "))   #Wind Chill
speed = float(input("Enter the wind speed (kilometer per hour): "))
p = pow(speed, 0.16)

wci = 13.12+(0.6215*temperature)-(11.37*p)+(0.3965*temperature*p)
print("Your Wind Chill Index: ", round(wci))
