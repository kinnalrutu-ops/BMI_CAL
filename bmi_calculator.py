
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = weight / (height ** 2)

print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 1))
