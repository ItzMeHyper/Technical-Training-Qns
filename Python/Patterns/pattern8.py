"""
if n = 4
            *
        *   *   *
    *   *   *   *   *
*   *   *   *   *   *   *
"""
n = int(input("Enter the number of rows & columns: "))

for i in range(n):
    for K in range(n - i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        print("*", end=" ")

    print()