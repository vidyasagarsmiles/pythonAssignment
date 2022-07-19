# Specified numbers in the list.
#

list = [1,20,24,35,19,88,2002,2003,1212]
print("List: ",list)
list2=[]
for i in range(0,len(list)-1):
    if list[i] % 2 == 0:
        #list.remove(list[i])
        print("removing: ", list[i])
    else:
        list2.append(list[i])

print(" List after removing even numbers from the list",list2)