# Calculating Body Mass Index for a person

weight = float(input("Enter Body Weight in kg: "))
height = float(input("Enter Body Height in m: "))

#metric
BMI = weight / (height**2)

print ("Your Body Mass Index BMI is: ", BMI)
