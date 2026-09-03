def tuple_examples():
    # Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Tuple:", my_tuple)

    # Accessing elements
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])

    # Slicing a tuple
    print("Slice from index 1 to 3:", my_tuple[1:4])

    # Tuple unpacking
    a, b, c, d, e = my_tuple
    print("Unpacked values:", a, b, c, d, e)

    # Length of a tuple
    print("Length of tuple:", len(my_tuple))

    # Checking if an element exists
    print("Does 3 exist in tuple?", 3 in my_tuple)

    # Concatenating tuples
    another_tuple = (6, 7, 8)
    combined_tuple = my_tuple + another_tuple
    print("Combined tuple:", combined_tuple)

    # Repeating tuples
    repeated_tuple = my_tuple * 2
    print("Repeated tuple:", repeated_tuple)

# Call the function to demonstrate tuple examples
tuple_examples()