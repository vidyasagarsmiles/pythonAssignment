#Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

def print_tuple_withsquares():
    tuple1=tuple([n*n for n in range(1,21)])
    return tuple1

print(print_tuple_withsquares())
