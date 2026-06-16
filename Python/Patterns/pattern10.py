"""
n=4
            *
        *       *
    *               *
*                       *
    *               *
        *       *
            *
"""

n = int(input("Enter the number of rows & columns: "))

for i in range(n):
    for k in range(n - i - 1):
        print(" ", end=" ")
    print("*", end=" ")

    for j in range(2 * i - 1):
        print(" ", end=" ")
    if i != 0:
        print("*", end=" ")
    print()

for i in range(n - 1):
    for k in range(i + 1):
        print(" ", end=" ")
    print("*", end=" ")

    for j in range(2 * (n - i - 2) - 1):
        print(" ", end=" ")
    if i != n - 2:
        print("*", end=" ")
    print()