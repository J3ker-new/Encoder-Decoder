### Encoder-Decoder in Python

This simple Python program encodes and decodes strings into binary representation and back. It takes a string as input, converts each character into its binary equivalent, and allows you to decode a list of binary values back into a string.

## Features

- **Encoding**: Converts each character of a string into its binary representation (Unicode code point).
- **Decoding**: Converts a list of binary strings back into the original string.

## How It Works

1. **Encoding**:
   - The program takes a string input from the user.
   - It converts each character into its Unicode code point (integer) and then into a binary string.
   - The binary representation is printed as a list of binary values.

2. **Decoding**:
   - The program prompts the user to enter a space-separated list of binary values.
   - It then converts each binary value back into the corresponding character and prints the decoded string.

## Example Usage

### Encoding:
Enter Name: Alice Encoded (binary representation): ['1000001', '1101100', '1100101', '1100010', '1100100']

### Decoding:
Enter the space-separated list of binary values: 1000001 1101100 1100101 1100010 1100100 Decoded (characters): ['A', 'l', 'i', 'c', 'e']

## Code Walkthrough

### Encoder
- **Input**: A string (e.g., `"Alice"`).
- **Process**: Each character is converted to its Unicode code point using `ord()` and then to a binary string using `bin()`.
- **Output**: A list of binary strings representing the encoded characters.

### Decoder
- **Input**: A list of binary values (space-separated).
- **Process**: Each binary string is converted back into its integer value using `int(binary_value, 2)` and then back to a character using `chr()`.
- **Output**: A list of characters decoded from the binary strings.

## Requirements
This program only requires Python 3.x. No external libraries are needed.

## Running the Program
1. Clone this repository or copy the code into a Python file (e.g., `encoder_decoder.py`).
2. Run the program using Python:
   ```bash
   python encoder_decoder.py
