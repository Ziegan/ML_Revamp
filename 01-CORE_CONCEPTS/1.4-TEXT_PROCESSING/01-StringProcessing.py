InputString = input("Enter the input String to perform String operations:\n")

def print_str(string):
    print(f"The Given String is: {string}")

def string_functions(string):
    print(f"Capitalized String: {string.capitalize()}")
    print(f"Casefold String: {string.casefold()}")
    print(f"Centerized String: {string.center()}")

    print(f"Is String L-Justified: {string.ljust()}")
    print(f"Is String R-Justified: {string.rjust()}")

    print(f"Count presence of \"A\": {string.count("A")}")
    print(f"Encoded String: {string.encode()}")

    print(f"Starts With A or not: {string.startswith("A")}")
    print(f"Ends With A or not: {string.endswith("A")}")
    
    print(f"Expandtabs to 5: {string.expandtabs(5)}")
    
    print(f"Find the position of \"Hello\" in the string: {string.find("Hello")}")
    print(f"R-Find the position of \"Hello\" in the string: {string.rfind("Hello")}")

    print(f"Return the index of \"Hello\" in the string: {string.index("Hello")}")
    print(f"R-Return the index of \"Hello\" in the string: {string.rindex("Hello")}")

    print(f"Splitting String based on delimiter \" \": {string.split(" ")}")
    print(f"R-Splitting String based on delimiter \" \": {string.rsplit(" ")}")

    print(f"Convert String to Title: {string.title()}")
    print(f"If String is Title: {string.istitle()}")

    print(f"Is String AlphaNumeric: {string.isalnum()}")
    print(f"Is String Alphabets: {string.isalpha()}")
    print(f"Is String ASCII: {string.isascii()}")
    print(f"Is String Decimal: {string.isdecimal()}")
    print(f"Is String Numbers: {string.isdigits()}")
    print(f"Is Valid String: {string.isidentifier()}")
    print(f"If Given String is Numerics: {string.numeric()}")
    print(f"Is the String printable: {string.isprinatble()}")
    print(f"If String is full of WhiteSpaces: {string.isspace()}")
    print(f"Joining iterables with the string: {string.join(["list"])}, {string.join("tuple")}, {string.join({"dict": "value"})}")

    print(f"InterChaning the Case for String: {string.swapcase()}")
    print(f"Changing the String to LowerCase: {string.lower()}")
    print(f"Changing the String to UpperCase: {string.upper()}")
    print(f"If Given String LowerCase: {string.islower()}")
    print(f"If Given String UpperCase: {string.isupper()}")

    print(f"Fill the String with 10 \"0\" on start: {string.zfill("10")}")

    print(f"Trim for the String: {string.strip()}")
    print(f"L-Trim for the String: {string.lstrip()}")
    print(f"R-Trim for the String: {string.rstrip()}")

    print(f"Translating the String S to A using ASCII CODE: {string.translate({83:  80})}")
    print(f"Translating the String H to A: {string.maketrans("H", "A")}")

    print(f"Make Partition Before/Identifier/After from the String: {string.partition(" ")}")
    print(f"Make R-Partition Before/Identifier/After from the String: {string.rpartition(" ")}")

    print(f"Replacing Chars H with A the String: {string.replace("H", "A")}")
    
def slice_strings(string):
    print(f"Sliced String from index 2 to 5: {string[2:5]}")

def slice_reverse(string):
    print(f"Reversing using string Slicing: {string[::-1]}")

def string_concardinate():
    string_1 = "Hello"
    string_2 = "World"

    string_3 = string_1 + string_2
    print("Printing Combined String:", string_3)
    
    string_3 = string_1 + " " + string_2
    print("Printing Combined String With Space Seperated:", string_3)

    