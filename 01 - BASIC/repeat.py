arr = [1,2,4,3,3,3]

duplicates = set([x for x in arr if arr.count(x) > 1])
print(duplicates)
