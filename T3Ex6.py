#
# Create a list with first and last 5 elements 
list=[]
for i in range(1,31):
    if i <=5:
        list.append(i*i)
    elif i > 25:
        list.append(i*i)
    else:
        list.append(i)

print(list)