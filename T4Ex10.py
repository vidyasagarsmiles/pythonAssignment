# Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

def even_number(x):
    return x%2==0

list1 = [n for n in range(1,21)]

print("Original List: ",list1)

even_list=filter(even_number,list1)

print("List with Even Numbers: ",list(even_list))