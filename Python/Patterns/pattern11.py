"""
n=5
                A
            B   A   B
        C   B   A   B   C
    D   C   B   A   B   C   D
E   D   C   B   A   B   C   D   E
"""
n = int(input("Enter the number of rows: "))

for i in range(n):
    for k in range(n - i - 1):
        print(" ", end=" ")

    for j in range(i, -1, -1):
        print(chr(65 + j), end=" ")
        
    for j in range(1, i + 1):
        print(chr(65 + j), end=" ")
    print()