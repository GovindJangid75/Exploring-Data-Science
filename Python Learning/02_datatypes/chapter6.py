# Chapter 6: Strings - Basic usage, Indexing, Slicing, Encoding

# Define a string variable
chai_type = "ginger chai"
# Define a customer name string
customer_name = "Garvita"

# Print formatted string using f-string
print(f"Order for {customer_name}, {chai_type} please!")

# Define a description string
chai_description = "aromatic and bold"

# Get the first word of the description using slicing and indexing
first_word = chai_description[0:8]  # 'aromatic' (0 to 7 inclusive, 8 not included)
print(f"First word: {first_word}")

# Get the last word of the description using slicing
last_word = chai_description[12:]  # from index 12 to end, 'bold'
print(f"Last word: {last_word}")

# Demonstrate slicing with step and skipping characters
every_second_char = chai_description[0:len(chai_description):2]
print(f"Every second character: {every_second_char}")

# Show that slicing with step = -1 reverses the string
reversed_description = chai_description[::-1]
print(f"Reversed description: {reversed_description}")

# Negative indexing example: going backwards in the string
# Not explicitly shown with variable, but similar to reversing string
print(f"Reversed (using negative step): {chai_description[::-1]}")

# Unicode string with special characters - example with Spanish-like characters
label_text = "Chai é spécial"

# Encoding the string into bytes using UTF-8 encoding
encoded_label = label_text.encode('utf-8')
print(f"Encoded label (bytes): {encoded_label}")

# Printing original label text (non-encoded)
print(f"Non-encoded label: {label_text}")

# Decoding the encoded bytes back to string
decoded_label = encoded_label.decode('utf-8')
print(f"Decoded label: {decoded_label}")
