my_list = [None, None, None, None, None, None, None, None, None, None]


def hash_make(values):
    tot_chars = 0
    for char in values:
        tot_chars += ord(char)
    hash_value = tot_chars % 10
    print("Hash value:", hash_value)
    return hash_value


def add_to_hash_table(value):
    index = hash_make(value)
    # my_list[index] = value  # rewrites the data on the hash table
    my_list[index].append(value)


def hash_contains(value):
    index = hash_make(value)
    return my_list[index] == value


print(my_list)

add_to_hash_table("asma")
print(my_list)

hash_contains("kuttima")
hash_contains("asma")
