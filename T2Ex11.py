## Exercise 11

counter = 1
luckyNumber = 12
while counter <= 5:
    num = int(input("Enter the lucky number: "))

    if num == luckyNumber:
        print("Good Guess")
        break
    else:
        print("Try Again")
    
    counter+=1


if counter >5:
    print("Sorry that was very unsuccesful")