# SITECOM-Decrypt

A Python script for XORing files. This can be used for simple encryption and decryption tasks.

## XOR Cipher Overview

The XOR cipher is a simple additive encryption algorithm. It operates by applying the exclusive OR (XOR) operation to every byte of the plaintext with a corresponding byte from a key. To decrypt the ciphertext, the same XOR operation is performed with the same key.

XOR ciphers are generally not considered secure for protecting sensitive information due_to their susceptibility to various cryptanalytic attacks. However, they can be useful for simple data obfuscation or educational purposes.

## Usage

To use the script, run it from your command line. You need to provide the path to the input file, the desired path for the output file, and the XOR key.

**Command format:**

```bash
python decrypt.py <input_filepath> <output_filepath> <xor_key>
```

**Arguments:**

*   `<input_filepath>`: The path to the file you want to XOR (encrypt/decrypt).
*   `<output_filepath>`: The path where the XORed output file will be saved.
*   `<xor_key>`: The key string to use for the XOR operation.

**Example:**

If you have a file named `encrypted_message.dat` and you want to decrypt it using the key `secret` and save the output as `decrypted_message.txt`, you would run:

```bash
python decrypt.py encrypted_message.dat decrypted_message.txt secret
```

## Requirements

[Details about any necessary prerequisites or dependencies will be listed here.]

## Contributing

[Guidelines for contributing to this project will be provided here.]
