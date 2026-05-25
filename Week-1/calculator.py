num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    sum = num1 + num2
    print("Sum: ", sum)

elif operation == "-":
    print("Difference: ", num1 - num2)

elif operation == "*":
    print("Product: ", num1 * num2)

elif operation == "/":
    print("Quotient: ", num1 / num2)
    
else:
    print("Invalid Operation!") 
