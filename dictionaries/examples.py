def create_dictionary_example():
    # Creating a sample dictionary
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
    
    # Accessing dictionary elements
    print("Name:", sample_dict['name'])
    print("Age:", sample_dict['age'])
    print("City:", sample_dict['city'])
    
    # Adding a new key-value pair
    sample_dict['job'] = 'Engineer'
    print("Updated Dictionary:", sample_dict)
    
    # Removing a key-value pair
    del sample_dict['age']
    print("Dictionary after deletion:", sample_dict)
    
    # Iterating through the dictionary
    for key, value in sample_dict.items():
        print(f"{key}: {value}")

# Call the function to demonstrate dictionary operations
create_dictionary_example()