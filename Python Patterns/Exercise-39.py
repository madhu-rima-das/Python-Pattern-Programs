#  Exercise 39 : (input : 5)
#
#  5
#  5 5
#  5 5 4
#  5 5 4 4
#  5 5 4 4 3
#  5 5 4 4 3 3
#  5 5 4 4 3 3 2
#  5 5 4 4 3 3 2 2
#  5 5 4 4 3 3 2 2 1
#  5 5 4 4 3 3 2 2 1 1
#
#
#
print("Exercise 39")
height = 5
for i in range(height * 2 , 0, -1):
    for j in range(height * 2, i-1, -1):
        if j%2 == 0:
            print(int(j/2), end = " ")
        else:
            print(int(j/2)+1, end = " ")
    print()
