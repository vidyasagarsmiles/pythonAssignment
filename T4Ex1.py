# Reverse the string.
#

n = input("Enter the string to reverse: ")

# print and reversing a string.
print(n[::-1])

# Using a for loop.
str=""

for x in range(len(n)-1,-1,-1):
    str+=n[x]
print(str)