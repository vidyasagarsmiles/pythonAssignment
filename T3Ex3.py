
list=[1,2,10,15,22]

print(sum(list))
multiply=0
for x in range(0,len(list)):
   if x==0:
    multiply=list[x]
   else:
        multiply=multiply*list[x]
print(multiply)