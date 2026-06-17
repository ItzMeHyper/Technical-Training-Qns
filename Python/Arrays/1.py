n = int(input("Enter the number of elements: "))

x = list(map(int, input("Enter the elements: ").split())) [:n] 
#[:n] is used to limit the number of elements to n, in case the user enters more than n elements.
print(x)