#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
num1 = float(input("Enter dividend: "))
num2 = float(input("Enter divisor: "))
if num2 != 0:
    print(f"Quotient: {num1 / num2}")
else:
    print("Cannot divide by zero.")
