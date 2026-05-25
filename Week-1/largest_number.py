a, b, c = map(int, input("Enter three numbers: ").split())

if a >= b and a >= c:
  print(f"{a} is the greatest.")

elif b >= a and b >= c:
  print(f"{b} is the greatest.")

else:
  print(f"{c} is the greatest.")
