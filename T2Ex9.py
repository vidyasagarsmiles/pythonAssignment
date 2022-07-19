# Guess lucky number.

luckyNumber=10
while True:
    num = int(input("Guess the Lucky Number: "))
    
    if num == luckyNumber:
        print("Guessed it correctly")
        break
    
    answer = input("Do you want to continue(yes/no)")
    if answer == 'no':
        break
        