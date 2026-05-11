input_string = input("Enter the Sentance to Calculate the Largest Word:\n")
words_list = input_string.split()
longest_word = ""
for word in words_list:
    if len(word) > len(longest_word):
        longest_word = word
print("the longest word is:",longest_word)
