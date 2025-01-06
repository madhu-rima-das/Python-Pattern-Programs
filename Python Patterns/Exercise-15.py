#  Exercise 15 : (height = 5)
#
#          *
#        * *
#      *   *
#    *     *
#  * * * * *
#
#
print("Exercise 15")
height=5
for i in range(height):
    for j in range(i,height-1):
        print(" ",end=" ")
    if i==0 or i==height-1:
        for j in range(i + 1):
            print("*", end=" ")
    else:
        for j in range(i + 1):
            if j==0 or j==i:
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()

print()


