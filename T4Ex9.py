# Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers

def showNumber(n):
    for i in range(0,n+1):
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")

input_num=int(input("Enter the number: "))
showNumber(input_num)