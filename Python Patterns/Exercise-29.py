#  Exercise 29 : (input : 5)
#
#  5 5 5 5 5
#  4 4 4 4
#  3 3 3
#  2 2
#  1
#
#
print("Exercise 29")
height=5
for i in range(height):
    for j in range(height-i):
        print(height-i,end=" ")
    print()
print()


