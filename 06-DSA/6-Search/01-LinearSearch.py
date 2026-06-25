mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

##VALUE BASED SEARCH
if 4 in mylist:
    print("Found!")
else:
    print("Not found!")


##INDEX BASED SEARCH
def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1


result = linearSearch(mylist, x)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")
