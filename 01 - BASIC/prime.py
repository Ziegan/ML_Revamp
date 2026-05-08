n = int(input("enter the given no"))

for i in range(2,n-1):

    if i % 2 == 0:
        print("non prime")
    break
else:
    print("prime")
