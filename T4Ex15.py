# Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def multiply(n):
    return n*n

list1 = [1,4,8,19,24,53]

multiples= list(map(multiply,list1))

print(multiples)
