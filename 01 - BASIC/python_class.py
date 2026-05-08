class addition:
    def add(self, a, b):
        return a + b


adding = addition()
input_1 = int(input("ENTER NUMBER A:"))
input_2 = int(input("ENTER NUMBER B:"))
resulting = adding.add(input_1, input_2)
print("ADDED VALUE IS:", resulting)
