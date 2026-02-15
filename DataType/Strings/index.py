"""indexing and slicing in strings
indexing in strings is the process of accessing individual characters in a string using their position or index. 
In Python, indexing starts at 0, which means that the first character of a string is at index 0, the second character is at index 1, and so on.
For example, if we have a string "Hello", we can access the first character 'H' using the index 0, the second character 'e' using the index 1, and so on. 
We can also use negative indexing to access characters from the end of the string,
where -1 refers to the last character, -2 refers to the second last character, and so on."""

name = "Hello, World!"
# Accessing characters using positive indexing
print(name[0])  # Output: H
print(name[7])  # Output: W
# Accessing characters using negative indexing
print(name[-1])  # Output: !    
print(name[-6])  # Output: W


