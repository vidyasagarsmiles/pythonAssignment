# Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].

input_list= [1,2,3,4,5,6,7,8,9,10]

def even_list_fn(x):
    return x%2==0

even_list = list(filter(even_list_fn,input_list))

squares_list= list(map(lambda n:n*n,even_list))

print(squares_list)

