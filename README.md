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

Running `run.bat` should give you the output (or something similar, if you altered the input file):

```
C:\Path\To\Dir>py -3 a51.py abc 0111110101101101110111011011110111001100101101001111001101100110
Encrypting...
Unprocessed Arguments
Key:  0111110101101101110111011011110111001100101101001111001101100110
Plaintext:  abc
Processing...
Processing complete.
Assigning Keys to Registers...
X:  0111110101101101110
Y:  1110110111101110011001
Z:  01101001111001101100110
Keystream:  000100111000110001000001
Plaintext:  011000010110001001100011
Binary Ciphertext:  011100101110111000100010
24
Normal Ciphertext:  rî"

Testing Results...
Unprocessed Arguments
Key:  0111110101101101110111011011110111001100101101001111001101100110
Plaintext:  rî"
Processing...
Processing complete.
Assigning Keys to Registers...
X:  0111110101101101110
Y:  1110110111101110011001
Z:  01101001111001101100110
Keystream:  000100111000110001000001
Plaintext:  011100101110111000100010
Binary Ciphertext:  011000010110001001100011
24
Normal Ciphertext:  abc

Test Result:  True
```
