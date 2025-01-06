#  Exercise 12 : (height = width = 5)
#
#  * * * * *
#  *       *
#  *       *
#  *       *
#  * * * * *
#

print("Exercise 12")
height = 5
width = 5
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            print("*", end=" ")
        else:
            if j == 0 or j == width -1:
                print("*", end=" ")
            else:
                print(" ", end = " ")
    print()
print()

