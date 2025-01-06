#  Exercise 7 : (height = 9 (any odd))
#
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#
print("Exercise 7")
star=9
if star%2==1:
    height=star//2

    for i in range(star-height+1):
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(height,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
else:
    print("the number you have entered is not an odd number")
print()

