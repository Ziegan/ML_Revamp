s = "pyhton interview is tricky"

word = s.split()

longest = ""

for word in word:
    if len(word) > len(longest):
        longest = word
print("the longest word is:",longest)
