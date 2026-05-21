name = input("Enter your name: ")

Mmarks = float(input("Enter your maths marks: "))
Emarks = float(input("Enter your english marks: "))
Smarks = float(input("Enter your science marks: "))

Tmarks = Mmarks + Emarks + Smarks 
average = Tmarks / 3

if average >= 80:
  grade = 'A'
  msg = 'Excellent work!'
  status = 'PASS'

elif average >= 70:
  grade = 'B'
  msg = 'Good job!'
  status = 'PASS'

elif average >= 60:
  grade = 'C'
  msg = 'Keep improving!'
  status = 'PASS'

else:
  grade = 'F'
  msg = "Don't give up!"
  status = 'FAIL'

print("\nRESULT\n")
print(f"Student's name: {name}\n\nEnglish marks: {Emarks} | Maths marks: {Mmarks} | Science marks: {Smarks}\nTotal: {Tmarks}\nAverage: {average:.2f}\n\nGrade: Grade {grade}\nStatus: {status}\n\n{msg}")