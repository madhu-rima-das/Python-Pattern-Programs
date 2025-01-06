#  Exercise 10 :
#
#      *         *         *         *
#     * *       * *       * *       * *
#    * * *     * * *     * * *     * * *
#   * * * *   * * * *   * * * *   * * * *
#  * * * * * * * * * * * * * * * * * * * *
#
#
print("Exercise 10")
height = 5
item = 4
for i in range(height):
    for j in range(i,height-1):
        print(" ",end="")
    for k in range(item):
        for j in range(i+1):
            print("*",end=" ")
        for j in range(i,height-1):
            print(" ",end=" ")
    print()
print()

