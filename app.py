import addition
import subtraction
import multiplication
import division

print("Choose an operation")
print("1. Add")
print ("2. Subtract")
print("3. Multiply")
print("4. Divide ")

userChoice = input ("Enter Choice 1 or 2 or 3 or 4  :  ")
if userChoice in ('1', '2', '3', '4'  ):
    number1 = float(input("Enter first number: "))
    number2 = float(input ("Enter second number: "))
    if userChoice == '1':
        print(number1, "+", number2, "=", addition.add(number1, number2))
    elif userChoice == '2':
        print(subtraction.subtract(number1,number2))
    elif userChoice == '3':
        print (multiplication.multiply(number1,number2))
    elif userChoice == '4':
        print(division.divide)
else:
    print("Invalid user input")