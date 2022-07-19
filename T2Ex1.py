# If a number divisible by 3- Print Consultadd
# If a number divisible  by 5 - print Python Training.
# if a number divisible by 3 and 5 - print consultadd-Python Training.

inputNumber=int(input("Enter the number: "))

if inputNumber % 3 == 0 and inputNumber % 5 == 0 :
    print("Consultad- Python Training.")
elif inputNumber % 5 == 0:
    print("Python Training")
elif inputNumber % 3 == 0:
    print("Consultad")
else:
    print("Not divisible by 3 and 5")
    