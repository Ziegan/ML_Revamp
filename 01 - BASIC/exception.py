try:
    number = int(input("Enter a number: "))
    print(10 / number)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
