num = [5,4,5,6,9]
num.sort()

print(num[-2])

arr = [1,2,4,3,3,3]

duplicates = set([x for x in arr if arr.count(x) > 1])
print(duplicates)
