input_string = input("Enter the String to Count Vowels:\n")
vowels = "aeiou"
count = 0
for char in input_string:
    if char in vowels:
        count += 1
print(f"Total Vowels Found {count} from the given string \"{input_string}\"")
