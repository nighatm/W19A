import addition
import subtraction
import multiplication
import divide

print("Please choose an operation")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

try:
    userChoice = int(input ("Enter Choice 1 or 2 or 3 or 4  :  "))
except:
    print ('You have entered an invalid option.')
else:
     if userChoice in ('1', '2', '3', '4'  ):
        number1 = int(input("Enter first number: "))
        number2 = int(input ("Enter second number: "))
        if (userChoice == '1'):
            print( "Result is: " str(addition.add(number1, number2)))
        elif (userChoice == '2'):
            print("Result is: " str(subtraction.subtract(number1, number2)))
        elif (userChoice == '3'):
            print ("Result is: " str(multiplication.multiply(number1, number2)))
        elif (userChoice == '4'):
            print("Result is: " str(divide.division(number1,number2)))    
    else:
        print("Invalid user input")
