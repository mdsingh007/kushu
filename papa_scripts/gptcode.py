# Define a function that takes a number of strings as input and returns the longest string
def longest_string(strings):
    # Initialize a variable to keep track of the longest string
    longest = ""

    # Loop through the input strings
    for string in strings:
        # If the current string is longer than the longest string so far,
        # update the longest string
        if len(string) > len(longest):
            longest = string

    # Return the longest string
    return longest

# Test the function by calling it with some strings
print(longest_string(["hello", "world", "this", "is", "a", "test"]))
print(longest_string(["this", "is", "a", "test", "of", "the", "function"]))
