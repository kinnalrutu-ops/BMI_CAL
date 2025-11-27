import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
else:
    script_name = "new"
    weight = 56
    height = 160   # in cm

# Convert cm to meters
height_m = height / 100

# Correct BMI formula
bmi = weight / (height_m ** 2)

print("Weight:", weight, "kg")
print("Height:", height_m, "m")
print("BMI:", round(bmi, 1))

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Overweight"

print("Category:", category)
