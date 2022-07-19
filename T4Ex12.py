#Write a function to compute 5/0 and use try/except to catch the exceptions
#
#

def fn_try_catch():
    num1 = 5
    num2 = 0
    try:
        div= num1/num2
        print("Division:",div)
    except Exception as e:
        print("Execption is: ",e)

fn_try_catch()