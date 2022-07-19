# Creating a dictionary that container number in x*x.

n = int(input("Enter the number:"))

dict={x: x*x for x in range(1,n+1)}
print(dict)