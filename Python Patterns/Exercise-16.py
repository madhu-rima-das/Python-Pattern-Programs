#  Exercise 16 : (height = 5)
#
#  * * * * *
#    *     *
#      *   *
#        * *
#          *
#
#
print("Exercise 16")
height=5
for i in range(height):
    for j in range(i):
        print(" ",end=" ")
    if i==0 or i==height-1:
        for j in range(i, height):
            print("*", end=" ")
    else:
        for j in range(i, height):
            if j==i or j==height-1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
    print()
print()

