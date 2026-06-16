num = int(input("Enter a number: "))

x = 0
y = 1

if num == 0:
    print(x)
elif num == 1:
    print(y)

for i in range(1,num):
    z = x + y
    x = y
    y = z
    
print(x)