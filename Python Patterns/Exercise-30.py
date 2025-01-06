#  Exercise 30 : (input : 5)
#
#  1
#  2 1
#  3 2 1
#  4 3 2 1
#  5 4 3 2 1
#
#
print("Exercise 30")
height=5
for i in range(height):
    for j in range(i+1):
        print(i-j+1,end=" ")
    print()
print()

