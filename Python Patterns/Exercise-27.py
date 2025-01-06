#  Exercise 27 : (input : 5)
#
#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1
#
#
print("Exercise 27")
height=5
for i in range(height):
    for j in range(height-i):
        print(j+1,end=" ")
    print()
print()

