# Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

def fn_divisble(x):
    if x%3 !=0 and x%7==0:
        return x

input_list=[27,32,86,49,54]

multiples= list(filter(fn_divisble,input_list))
print(multiples)