x = 123
for i in x:
    print(i)

# Returns an error: int object is not iterable.


i=0
while i<5:
    print(i)
    i+=1
    if i == 3:
        break
    else:
        print("error")

# Output:
# 0
# error
# 1
# error
# 2

count = 0
while True:
    print(count)
    count+=1
    if count >=5:
        break

# Output:
# 0 1 2 3 4 
