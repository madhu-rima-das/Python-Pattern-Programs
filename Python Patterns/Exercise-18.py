#  Exercise 18 : (height = 6)
#
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  * * * * * *
#
#
print("Exercise 18")
height=6
for i in range(height):
    for j in range(i,height-1):
        print(" ",end="")
    if i==0 or i==height-1:
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(i+1):
            if j==0 or j==i:
                print("*", end=" ")
            else:
                print(" ",end=" ")

    print()
print()

