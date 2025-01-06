#  Exercise 6 : (height = 6)
#
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
#
#
print("Exercise 6")
height=6
for i in range(height):
    for j in range(i,height-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
print()
