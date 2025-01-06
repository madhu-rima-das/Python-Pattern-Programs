#  Exercise 8 : (height = 9 (any odd))
#
#          *
#        * *
#      * * *
#    * * * *
#  * * * * *
#    * * * *
#      * * *
#        * *
#          *
#
print("Exercise 8")
star=9
if star%2==1:
    height=star//2
    for i in range(height+1):
        for j in range(i, height):
            print(" ", end=" ")

        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(height):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(height, i, -1):
            print("*", end=" ")
        print()
else:
    print("the number you have entered is not an odd number")
print()

