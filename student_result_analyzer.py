n = int(input("Enter number of students: "))

total = 0
high = 0
low = 100
fail = 0
pass_ = 0

print("\nEnter the marks of the students: ")

for i in range(1, n + 1):
  mark = float(input(f"Student {i}: "))
  total = total + mark

  if mark > high:
    high = mark
  if mark < low:
    low = mark

  if mark < 50:
    fail += 1
  else:
    pass_ += 1

  if mark >= 50:
    if mark >= 90:
      grade = 'A+'
    elif mark >= 80:
      grade = 'A'
    elif mark >= 70:
      grade = 'B'
    elif mark >= 60:
      grade = 'C'
    else:
      grade = 'D'
  else:
    grade = 'F'
  
  print("Grade ", grade)

print("\n*****STUDENT RESULT ANALYSIS*****")

print("\nTotal marks of all student: ", total)

avg = total / n
print("Average marks: ", avg)

print("\nHighet marks: ", high)
print("Lowest marks: ", low)

print("\nPassed students: ", pass_)
print("Failed students: ", fail)
