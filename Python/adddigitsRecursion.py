def addDigits(num):
    if num < 10:
        return num
    
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem
        num //= 10
    return addDigits(sum)

num = int(input("Enter a number: "))
result = addDigits(num)
print(result)