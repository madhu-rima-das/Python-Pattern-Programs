#  Exercise 22 :
#
#      *         *         *         *
#     * *       * *       * *       * *
#    *   *     *   *     *   *     *   *
#   *     *   *     *   *     *   *     *
#  * * * * * * * * * * * * * * * * * * * *
#
#
#
print("Exercise 22")
height=5
for i in range(height):
    for j in range(i,height-1):
        print(" ",end="")
    for k in range(4):
        if i == 0 or i == height - 1:
            for j in range(i + 1):
                print("*", end=" ")
        else:
            for j in range(i + 1):
                if j == 0 or j == i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        for j in range(i,height-1):
            print(" ",end=" ")
    print()
print()

