# Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.

string = input("Enter the string to calculate num of upper and lower cases: ")

upper = 0
lower = 0

for x in range(0,len(string)):
    if string[x].isupper():
        upper+=1
    elif string[x].islower():
        lower+=1
    else:
        continue

print("Num of Upper Case letter: ",upper,"Num of lower case letter: ",lower)
