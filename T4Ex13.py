#
# Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools

def flatten():
    input_list=[1,2,3,4,5,6,7]
    print(functools.reduce(lambda a,b:str(a)+str(b),input_list))

flatten()
