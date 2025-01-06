#  Exercise 36 : (input : 5)
#
#          1
#        2 1 2
#      3 2 1 2 3
#    4 3 2 1 2 3 4
#  5 4 3 2 1 2 3 4 5
#
#
#
print("Exercise 36")
height = 5
for i in range(1, height+1):
    for j in range(height - i):
        print(" ", end = " ")
    k = i
    m = 1
    for j in range( 2*i-1):
        if k > 1:
            print(k, end = " ")
            k-=1
        else:
            print(m, end = " ")
            m+=1
    print()
