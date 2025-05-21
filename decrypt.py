import argparse
from itertools import cycle

def xor(input_data, xor_key):
    """
    Performs XOR operation on input_data using xor_key.

    Args:
        input_data: The data to be XORed (string).
        xor_key: The key to use for XORing (string).

    Returns:
        The XORed data (string).
    """
    # The cycle function ensures that the key is repeated if it's shorter than the data.
    return ''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip(input_data, cycle(xor_key)))

def decrypt_file(input_filepath, output_filepath, key_string):
    """
    Reads an input file, XORs its content with the provided key, and writes the result to an output file.

    Args:
        input_filepath: Path to the input file.
        output_filepath: Path to the output file.
        key_string: The XOR key string.
    """
    try:
        # Open the input file in binary read mode ('rb')
        with open(input_filepath, 'rb') as input_file:
            # Read the entire content of the input file
            encrypted_data = input_file.read()
        
        # Perform the XOR operation. Note: The current xor function expects strings.
        # If the file is binary, this might lead to issues with chr(ord(a) ^ ord(b)) if the result is not a valid char.
        # For robust binary XORing, we should work with bytes directly.
        # However, sticking to the original xor function's string-based nature for now.
        # The file is read as bytes, so we need to decode it to string before XORing, assuming it's decodable (e.g., UTF-8).
        # And then encode the result back to bytes before writing. This is a common source of errors if encoding is not handled carefully.
        decrypted_data_str = xor(encrypted_data.decode('latin-1'), key_string) # Assuming latin-1 to handle arbitrary bytes as chars

        # Open the output file in binary write mode ('wb')
        with open(output_filepath, 'wb') as output_file:
            # Write the decrypted data to the output file
            output_file.write(decrypted_data_str.encode('latin-1')) # Encode back to latin-1
        
        print(f"File '{input_filepath}' decrypted successfully to '{output_filepath}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="XORs a file with a given key.")
    
    # Add arguments
    parser.add_argument("input_filepath", help="Path to the input file to be XORed.")
    parser.add_argument("output_filepath", help="Path to the output file to store the XORed result.")
    parser.add_argument("xor_key", help="The XOR key string.")
    
    # Parse arguments from the command line
    args = parser.parse_args()
    
    # Call the main function with parsed arguments
    decrypt_file(args.input_filepath, args.output_filepath, args.xor_key)
