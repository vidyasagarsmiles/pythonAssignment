# Swapping with third variable.

x,y = 5,7
print("Before swapping")
print("x =",x,"y =",y)
temp=x
x=y
y=temp
print("After Swapping")
print("x =",x,"y =",y)


# No Third Variable.
x,y = 5,9
print("Before Swapping")
print("x =",x,"y =",y)
x,y=y,x
print("After Swappping")
print("x =",x,"y =",y)
