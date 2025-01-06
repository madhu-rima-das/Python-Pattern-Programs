#  Exercise 5 : (height = 6)
#
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
#
print("Exercise 5")
height=6
for i in range(height):
    for j in range(i):
        print(" ",end="")
    for j in range(i, height):
        print("*",end=" ")
    print()
print()
