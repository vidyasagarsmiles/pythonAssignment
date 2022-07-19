# 
# Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list_fn(list):
    unique_list=[]
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

x = [1,1,2,3,4,5,5,6,8,10]

print(unique_list_fn(x))
