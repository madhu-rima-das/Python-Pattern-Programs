#  Exercise 13 : (height = 5)
#
#  *
#  * *
#  *   *
#  *     *
#  * * * * *
#

print("Exercise 13")
height=5
for i in range(height):
    if i == height-1:
        for j in range(i + 1):
            print("*", end=" ")
    else:
        for j in range(i+1):
            if j == 0 or j == i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
print()


