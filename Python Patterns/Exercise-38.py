#  Exercise 38 : (input : 5)
#
#  1
#  1 2 1
#  1 2 3 2 1
#  1 2 3 4 3 2 1
#  1 2 3 4 5 4 3 2 1
#
#
print("Exercise 38")
height = 5
for i in range(1, height+1):
    k = 1
    m = i
    for j in range(2 * i - 1):
        if k < i:
            print(k, end=" ")
            k += 1
        else:
            print(m, end=" ")
            m -= 1
    print()