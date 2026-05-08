s = input("enter the given str")

count = 0

for ch in s:
    if ch in 'aeiou':
        count += 1
print("the ovewl",count)
