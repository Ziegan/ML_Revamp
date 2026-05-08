n = int(input("enter the no"))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
