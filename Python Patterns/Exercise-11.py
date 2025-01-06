#  Exercise 11 : (height = 9, width = 10)
#
#  * * * * * * * * * *
#   * * * * * * * * * *
#  * * * * * * * * * *
#   * * * * * * * * * *
#  * * * * * * * * * *
#   * * * * * * * * * *
#  * * * * * * * * * *
#   * * * * * * * * * *
#  * * * * * * * * * *
#
#
print("Exercise 11")
height=9
width = 10
for i in range(height):
    for j in range(width):
        if i % 2 == 0:
            print("* ",end="")
        else:
            print(" *", end="")
    print()
print()

