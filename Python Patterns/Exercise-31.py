#  Exercise 31 : (input : 5)
#
#  5 4 3 2 1
#  4 3 2 1
#  3 2 1
#  2 1
#  1
#
#
print("Exercise 31")
height=5
for i in range(height):
    for j in range(height-i):
        print(height-i-j,end=" ")
    print()


