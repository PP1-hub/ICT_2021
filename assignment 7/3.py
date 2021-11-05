weight = int(input('weight:'))
height = float(input('height:'))

BMI = weight / (height * height)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You have a normal weight")
elif BMI <= 29.9:
    print("You are slightly overweight")
elif BMI <= 34.9:
    print("You are obese")
else:
    print("You are clinically obese")         
    
          