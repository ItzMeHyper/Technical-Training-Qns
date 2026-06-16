"""
if n = 4 
1 
2 3 
4 5 6 
7 8 9 10 
"""

n = int(input("Enter the number of rows & columns: "))
num = 0

for i in range(n):
    for j in range(i + 1):
        num+=1
        print(num, end=" ")
    print()