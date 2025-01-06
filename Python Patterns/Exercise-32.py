#  Exercise 32 : (input : 5)
#
#          1
#        1 2
#      1 2 3
#    1 2 3 4
#  1 2 3 4 5
#
#
print("Exercise 32")
height = 5
for i in range(1, height+1):
    for j in range(height - i):
        print(" ", end = " ")
    for j in range(i):
        print(j+1, end = " ")
    print()

