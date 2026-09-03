def string_examples():
    # Example of string manipulation
    sample_string = "Hello, World!"
    
    # Convert to uppercase
    upper_string = sample_string.upper()
    
    # Convert to lowercase
    lower_string = sample_string.lower()
    
    # Find the length of the string
    string_length = len(sample_string)
    
    # Replace a substring
    replaced_string = sample_string.replace("World", "Python")
    
    # Split the string into a list
    string_list = sample_string.split(", ")
    
    # Join a list into a string
    joined_string = " - ".join(string_list)
    
    # Print results
    print("Original String:", sample_string)
    print("Uppercase:", upper_string)
    print("Lowercase:", lower_string)
    print("Length:", string_length)
    print("Replaced String:", replaced_string)
    print("String List:", string_list)
    print("Joined String:", joined_string)

# Call the function to demonstrate string examples
string_examples()