#  Exercise 14 : (height = 5)
#
#  * * * * *
#  *     *
#  *   *
#  * *
#  *
#

print("Exercise 14")
height2=5
for i in range(height2,0,-1):
    if i==height2:
        for j in range(i):
            print("*", end=" ")
    else:
        for j in range(i):
            if j==0 or j==i-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
print()


