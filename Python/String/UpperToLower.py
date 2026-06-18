#Uppercase to Lowercase without using built-in functions
s = input()
l = ""
for char in s:
    #if 'A' <= char <= 'Z':
    if ord(char) < 97:
        l += chr(ord(char) + 32)
    else:
        l += char
print(l)