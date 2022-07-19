# Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
#

def print_string_with_maxLen():
    string_1=input("Enter the string one: ")
    string_2=input("Enter the String two: ")

    if len(string_1) == len(string_2):
        print(string_1)
        print(string_2)
    else:
        print(max(string_1,string_2,key=len))
    
print_string_with_maxLen()