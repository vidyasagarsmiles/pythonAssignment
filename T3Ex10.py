# Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string 

n = input("enter a list of numbers")

list1 = n.split(',')
set1 = tuple(list1)

print("list",list1)
print("set",set1) 