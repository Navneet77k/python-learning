def set_operations_example():
    # Creating a set
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)

    # Adding an element
    my_set.add(6)
    print("After Adding 6:", my_set)

    # Removing an element
    my_set.remove(3)
    print("After Removing 3:", my_set)

    # Checking membership
    print("Is 2 in the set?", 2 in my_set)

    # Set union
    another_set = {4, 5, 6, 7, 8}
    union_set = my_set.union(another_set)
    print("Union of sets:", union_set)

    # Set intersection
    intersection_set = my_set.intersection(another_set)
    print("Intersection of sets:", intersection_set)

    # Set difference
    difference_set = my_set.difference(another_set)
    print("Difference of sets:", difference_set)

if __name__ == "__main__":
    set_operations_example()