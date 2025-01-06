#  Exercise 34 : (input : 5)
#
#  1 2 3 4 5
#  2 3 4 5
#  3 4 5
#  4 5
#  5
#
#
print("Exercise 34")
height = 5
for i in range(1, height+1):
    for j in range(i, height+1):
        print(j, end = " ")
    print()