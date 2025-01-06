#  Exercise 35 : (input/height : 6)
#
#        1
#       2 2
#      3 3 3
#     4 4 4 4
#    5 5 5 5 5
#   6 6 6 6 6 6
#
#
#
print("Exercise 35")
height = 6
for i in range(1, height+1):
    for j in range(i, height+1):
        print(" ", end = "")
    for j in range(1, i+1):
        print(i, end = " ")
    print()
