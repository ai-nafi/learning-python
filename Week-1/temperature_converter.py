temp = input("Type 'C' if you want to convert to celsius and type 'F' if you want to convert to fahrenheit: ")

if temp == 'C':
  F = float(input("Give the temperature in fahrenheit: "))
  C = (F - 32) * 5/9
  print(f"The temperature in celsius is {C}")

elif temp == 'F':
  C = float(input("Give temperature in celsius: "))
  F = (C * 9/5) + 32
  print(f"The temperature in fahrenheit is {F}")

else:
  print("Invalid input!")
