marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
  print("Enter correct marks")

elif marks >= 80:
  print("Grade A")

elif marks >= 70:
  print("Grade B")

elif marks >= 60:
  print("Grade C")

else:
  print("Fail")
