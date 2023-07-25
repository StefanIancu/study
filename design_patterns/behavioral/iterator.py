

def count_to(count):
    # iterator implementation 

    # list 
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # built-in iterator, creates tuple (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # iterate through iterable list, extract numbers, put them in a generator caller number
    for position, number in iterator:
        yield number

# test generator returned by iterator
for num in count_to(3):
    print(f"{num}")

# for num in count_to(5):
#     print(f"{num}")