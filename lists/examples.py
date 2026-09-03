def list_examples():
    # Creating a list
    fruits = ['apple', 'banana', 'cherry']
    
    # Accessing elements
    first_fruit = fruits[0]
    
    # Adding an element
    fruits.append('orange')
    
    # Removing an element
    fruits.remove('banana')
    
    # Iterating through the list
    for fruit in fruits:
        print(fruit)
    
    # List length
    length = len(fruits)
    
    # List slicing
    sliced_fruits = fruits[1:3]
    
    return first_fruit, length, sliced_fruits

if __name__ == "__main__":
    first_fruit, length, sliced_fruits = list_examples()
    print(f"First fruit: {first_fruit}")
    print(f"Number of fruits: {length}")
    print(f"Sliced fruits: {sliced_fruits}")