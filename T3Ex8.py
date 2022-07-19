# Concatinating two dictionaries.
# print the output as one.

a = {1:10,2:20,3:30}
b = {4:40,5:50}
c={}
c= {**a,**b}
print(c)