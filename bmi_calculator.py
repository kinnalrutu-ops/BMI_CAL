
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = weight / (height ** 2)

print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 1))

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Overweight"

print("Category:", category)
