def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before calling the functions")
        func(*args, **kwargs)
        print("Decorator: After Calling the functions")
    return wrapper


@decorator
def testing(a):
    print("Function Invoked, Value to printback is:", a)

testing(input("print the value to printback: \n"))