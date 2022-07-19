# Perform Arithmetic operations in python.
# Enter 1 - Addition.
# Enter 2 - Subtraction.
# Enter 3 - Division.
# Enter 4 - Multiplication.
# Enter 5 - Average.

def checkNegative(result):
    if result < 0:
        print("NEGATIVE")


print("Enter 1 - Addition")
print("Enter 2 - Subtraction")
print("Enter 3 - Division")
print("Enter 4 - Multiplication")
print("Enter 5 - Average")

option=int(input("Enter the option: "))
 
num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))

if option == 1:
    result= num1+num2
    print("Addition of",num1,"and",num2,"is:",result)
    checkNegative(result)
elif option == 2:
    result= num1-num2
    print("Subration of",num1,"and",num2,"is:",result)
    checkNegative(result)
elif option == 3:
    result= num1/num2
    print("Division of",num1,"by",num2,"is:",result)
    checkNegative(result)
elif option == 4:
    result= num1*num2
    print("Multiplication of ", num1,"and",num2,"is:",result)
    checkNegative(result)
elif option == 5:
    num3= int(input("Enter third number for average: "))
    num4= int(input("Enter the fourth number for Average: "))
    result = (num1+num2+num3+num4)/4
    print("Average of",num1,num2,num3,num4,"is: ",result)
    checkNegative(result)
else:
    print("Please enter the correct option ")


