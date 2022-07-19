# Write a program in a loop with break and continue.

while(True):
    x=int(input("Enter a number: "))
    if x > 0: 
        print("The entered number is ",x)
        print("Get going")
        continue
    elif x < 0:
        print("The entered number is ",x)
        print("It's over.")
        break
