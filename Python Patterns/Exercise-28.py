#  Exercise 28 : (input/height : 5)
#
#  1
#  3 3
#  5 5 5
#  7 7 7 7
#  9 9 9 9 9
#
#
print("Exercise 28")
height=5
for i in range(1,height+1):
    for j in range(1,i+1):
        print(i*2-1,end=" ")
    print()
print()

