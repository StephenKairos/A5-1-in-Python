# A5-1-in-Python
A5/1 Implementation in Python for CS 166 (Cryptography) at SJSU

This was an implementation for one of the Extra Credit assignments for CS 166. It's a crude cli implementation of the hardware-based A5/1 stream cipher.

It does a few things:

1. Processes a source string to encrypt with a binary key with a length of 64 bits.
2. Splits and assigns the key into 3 registers: 19, 22, and 23 bits in length.
3. Converts the plaintext string parameter into raw binary data.
4. Generates a keystream with the same length as the input plaintext binary.
5. Produces the ciphertext with the use of XOR.

It will do this both to encrypt the data and decrypt it, and compares the resulting plaintext with the initial input. 
