## Exercise 10

counter = 1
luckyNumber = 12
while counter <= 5:
    num = int(input("Enter the lucky number: "))

    if num == luckyNumber:
        print("Good Guess")
    else:
        print("Try Again")
    
    counter+=1

print("Game Over")
