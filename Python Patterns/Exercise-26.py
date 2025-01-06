#  Exercise 26 : (input : 5, so, height will be 5 as well)
#
#  5 5 5 5 5
#  5 5 5 5
#  5 5 5
#  5 5
#  5
#
#

print("Exercise 26")
height = 5
for i in range(height):
    for j in range(height - i):
        print(height, end = " ")
    print()
print()


