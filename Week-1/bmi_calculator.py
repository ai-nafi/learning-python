print("Hello! Let's calculate your BMI.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

if weight <= 0 or height <= 0:
  print("Please enter valid weight and height")

else:
  bmi = weight / (height * height)

  if bmi < 18.5:
    print(f"Your BMI is {bmi} and you're underweight")

  elif bmi >= 18.5 and bmi < 24.9:
    print(f"Your BMI is {bmi} and you have a normal weight")

  elif bmi >= 25 and bmi < 29.9:
    print(f"Your BMI is {bmi} and you're overweight")

  else:
    print(f"Your BMI is {bmi} and you're obese")
