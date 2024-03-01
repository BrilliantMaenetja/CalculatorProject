#####Simple Calculator#####

firstNumber = float(input("Enter first number : "))

secondNumber = float(input("Enter second number : "))
 
operator = input("Enter a Mathematical Operator : ")

answer = 0 

if operator == "+":
    answer = firstNumber +  secondNumber
    print("Sum = " , answer)

elif operator == "*" :
    answer = firstNumber * secondNumber
    print("Pruduct = " , answer )
    
elif operator == "/":
    answer = firstNumber / secondNumber
    print("Division = " , answer)
 
elif operator == "-":
    answer = secondNumber - firstNumber
    print("Difference = " , answer)

else :
    print("You didn't enter a valid operator")    
    
        