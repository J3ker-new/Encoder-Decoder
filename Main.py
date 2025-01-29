# Encoder
# Prompt the user to enter a name (or string)
name = input("Enter Text To Be Encoded: ")

# Create an empty list 'array' with the same length as the input 'name'
# This will hold the binary representations of each character in the name
array = [None] * len(name)

# Loop through each character in the input 'name'
for i in range(len(name)):
    # Convert the character to its Unicode code point (integer) using ord()
    # Then convert that integer to its binary representation using bin()
    # [2:] removes the '0b' prefix from the binary string
    array[i] = bin(ord(name[i]))[2:]

# Print the resulting list of binary representations
print("Encoded (binary representation):", array)


# Decoder
# Prompt the user to enter the space-separated list of binary values (encoded characters)
user = input("Enter the space-separated list of binary values: ")

# Split the input string into a list of binary values by separating at spaces
myList = user.split()  

# Create an empty list to store the decoded characters
decoded_list = []

# Loop through each binary value in 'myList'
for binary_value in myList:
    # Convert the binary value (a string) back to an integer using int(binary_value, 2)
    # The '2' tells Python that the input string is in binary format
    # Convert the integer back to the corresponding character using chr()
    decoded_list.append(chr(int(binary_value, 2)))

# Print the decoded list of characters
print("Decoded (characters):", decoded_list)
input("Press any key to continue:")