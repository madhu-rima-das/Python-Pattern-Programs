#  Exercise 3 : (height = 5)
#
#          *
#        * *
#      * * *
#    * * * *
#  * * * * *
#
print("Exercise 3")
height=5
for i in range(height):
    for j in range(i,height-1):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")
    print()

print()


