def first_letter_to_appear_twice(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        else:
            seen.add(char)
    return None

n = input("Enter a string: ")
result = first_letter_to_appear_twice(n)
print("The first letter to appear twice is:", result)
    