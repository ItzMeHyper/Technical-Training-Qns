num = int(input("Enter a number: "))

x = 0
y = 1

for i in range(1,num):
    z = x + y
    x = y
    y = z
    
print(x)