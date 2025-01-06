#  Exercise 33 : (input : 5)
#
#  1 2 3 4 5
#  2 2 3 4 5
#  3 3 3 4 5
#  4 4 4 4 5
#  5 5 5 5 5
#
#
print("Exercise 33")
height = 5
for i in range(1, height+1):
    for j in range(1, height+1):
        if j>=i:
            print(j, end = " ")
        else:
            print(i, end = " ")
    print()