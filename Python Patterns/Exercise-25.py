#  Exercise 25 : (input : 5)
#
#  1 1 1 1 1
#  2 2 2 2
#  3 3 3
#  4 4
#  5
#
#

print("Exercise 25")
height = 5
for i in range(height):
    for j in range(i, height):
        print(i + 1, end = ' ')
    print()
print()

