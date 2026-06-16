"""
n=4
            *
        *   *   *
    *   *   *   *   *
*   *   *   *   *   *   *
    *   *   *   *   *
        *   *   *
            *
"""

n = int(input("Enter the number of rows & columns: "))
for i in range(n):
    for K in range(n - i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

for i in range(n - 1):
    for K in range(i + 1):
        print(" ", end=" ")

    for j in range(2 * (n - i - 1) - 1):
        print("*", end=" ")
    print()