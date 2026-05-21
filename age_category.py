age = int(input("Enter your age: "))

if age > 0 and age <= 13:
  print("You are a child")

elif age >= 14 and age <= 18:
  print("You are a teenager")

else:
  print("Your are an adult")