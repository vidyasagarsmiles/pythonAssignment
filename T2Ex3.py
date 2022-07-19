#
#
#
#
#

print("Enter three number to calculate the average")
a=int(input("Enter number 1: "))
b=int(input("Enter Number 2: "))
c=int(input("Enter Number 3: "))

average=(a+b+c)/3
print("Average: ",average)

if average > a and average > b and average > c:
    print("Average is higher than abc")
elif average >  a and b:
    print("Average is higher than a and b")
elif average >  a and c:
    print("Average is higher than a and c")
elif average > b and c:
    print("Average is higher than b and c")
elif average > a:
    print("Average is just higher than a")
elif average > b:
    print("Average is just higher than b")
elif average > c:
    print("Average is just higher than c")