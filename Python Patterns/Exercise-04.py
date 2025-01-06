#  Exercise 4 : (height = 5)
#
#  * * * * *
#    * * * *
#      * * *
#        * *
#          *
#
print("Exercise 4")
height=5
for i in range(height):
    for j in range(i):
        print(" ",end=" ")
    for j in range(height,i,-1):
        print("*",end=" ")
    print()
print()


