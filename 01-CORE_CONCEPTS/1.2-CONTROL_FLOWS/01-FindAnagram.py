s1 = input("Enter the String 1:")
s2 = input("Enter the String 2:")

if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("non anagram")