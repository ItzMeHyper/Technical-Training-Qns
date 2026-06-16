num = int(input("Enter a number: "))

while num >= 10:
    sum = 0

    while num > 0:
        rem = num % 10
        sum += rem
        num //= 10

    num = sum

print(num)