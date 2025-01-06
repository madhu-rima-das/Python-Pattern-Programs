#  Exercise 19 : (height = 9 (any odd))
#
#  *
#  * *
#  *   *
#  *     *
#  *       *
#  *     *
#  *   *
#  * *
#  *
#
#
#
print("Exercise 19")
star=9
if star%2==1:
    height=star//2

    for i in range(height+1):
        for j in range(i + 1):
            if j == 0 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(height):
        for j in range(i,height):
            if j == i or j == height - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("the number you have entered is not an odd number")
print()

