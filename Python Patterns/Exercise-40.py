#  Exercise 40 : (input : 10)
#
#  0
#  1 0
#  0 1 0
#  1 0 1 0
#  0 1 0 1 0
#  1 0 1 0 1 0
#  0 1 0 1 0 1 0
#  1 0 1 0 1 0 1 0
#  0 1 0 1 0 1 0 1 0
#  1 0 1 0 1 0 1 0 1 0
#
#
#
print("Exercise 40")
height = 10
for i in range(1 , height+1):
    for j in range(1, i+1):
        if i%2 != 0:
            if j%2 == 0:
                print("1", end = " ")
            else:
                print("0", end = " ")
        else:
            if j%2 == 0:
                print("0", end = " ")
            else:
                print("1", end = " ")
    print()
