###TYPES
x = str("Hello World")
print(f"String: {x}, {type(x)}")

x = int(20)
print(f"Number: {x}, {type(x)}")

x = float(20.5)
print(f"Float: {x}, {type(x)}")

x = complex(1j)
print(f"Complex: {x}, {type(x)}")

x = list(("apple", "banana", "cherry"))
print(f"List: {x}, {type(x)}")

x = tuple(("apple", "banana", "cherry"))
print(f"Tuple: {x}, {type(x)}")

x = dict(name="John", age=36)
print(f"Dict: {x}, {type(x)}")

x = set(("apple", "banana", "cherry"))
print(f"Set: {x}, {type(x)}")

x = frozenset(("apple", "banana", "cherry"))
print(f"FrozenSet: {x}, {type(x)}")

x = bool(5)
print(f"Bool: {x}, {type(x)}")

x = bytes(5)	
print(f"Bytes: {x}, {type(x)}")

x = bytearray(5)
print(f"ByteArray: {x}, {type(x)}")

x = memoryview(bytes(5))
print(f"MemoryView: {x}, {type(x)}")

x = range(6)
print(f"Range: {x}, {type(x)}")

###TYPE_CASTING
##INT CASTING
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print("INT: ", x,y,z)

##FLOAT CASTING
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print("FLOAT: ", x,y,z,w)

##STRING CASTING
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'