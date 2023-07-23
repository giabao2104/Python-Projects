def swap(a, b):
    a, b = b, a
    return a, b

a = 3
b = 5
a, b = swap(b, a)
print(a, b)