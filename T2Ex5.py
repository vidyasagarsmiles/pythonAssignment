# Print numbers which are divisble by 7 and not a multiple  of 5.
# in range between 2000, 3200.
#

for x in range(2000,3201):
    if x % 7 == 0 and x % 5 != 0:
        print(x)
    