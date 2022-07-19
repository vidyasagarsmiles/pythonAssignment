x = input("Enter the String")
alpha=0
digits=0
for i in x:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digits+=1

print("Letters: ",alpha)
print("Digits",digits)