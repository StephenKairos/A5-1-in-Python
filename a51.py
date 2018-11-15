import re
import sys
from argparse import *

def main(args):
	file = open("output.txt", "w+")

	print("Unprocessed Arguments")
	print("Key: ", args.key)
	print("Plaintext: ", args.plaintext)
	print("Processing...")
	# parse the key and check if it's valid
	if len(args.key) != 64:
		print("Key is not 64-digits")
		return
	key = re.sub('[^01]', '', args.key)
	if len(args.key) != 64:
		print("Key had invalid characters, only 0 or 1")
		return
	print("Processing complete.")

	print("Assigning Keys to Registers...")
	key_x = key[:19]
	key_y = key[19:-23]
	key_z = key[-23:]

	print('X: ', key_x)
	print('Y: ', key_y)
	print('Z: ', key_z)

	keystream = ''

	for i in range(len(args.plaintext) * 8):
		majority = maj(key_x, key_y, key_z) # Majority Vote

		if majority != 3 or majority != 4:
			key_x = step_x(key_x)
		if majority != 2 or majority != 5:
			key_y = step_y(key_y)
		if majority != 1 or majority != 6:
			key_z = step_z(key_z)

		keystream = keystream + str(next_bit(key_x, key_y, key_z))

	b_plaintext = string_to_binary(args.plaintext)

	print("Keystream: ", keystream)
	print("Plaintext: ", b_plaintext)

	ciphertext = ''

	for i in range(len(b_plaintext)):
		k = int(keystream, 2) >> i & 1
		p = int(b_plaintext, 2) >> i & 1
		ciphertext = str((k ^ p)) + ciphertext
	# Binary
	print("Binary Ciphertext: ", ciphertext)
	# As Characters
	chr_ciphertext = ''

	print(len(ciphertext))

	for i in range(int(len(ciphertext) / 8)):
		chr_ciphertext = chr_ciphertext + chr(int(ciphertext[i * 8:(i + 1) * 8], 2))
	
	print("Normal Ciphertext: ", chr_ciphertext)
	#file.write(chr_ciphertext)

	return chr_ciphertext

def maj(key_x, key_y, key_z):
	x = int(key_x, 2) >> 10 & 1 # Gets 8th bit
	y = int(key_y, 2) >> 11 & 1 # Gets 10th bit
	z = int(key_z, 2) >> 12 & 1 # Gets 10th bit
	# We'll decode the votes, like a binary decoder
	vote = (x << 2) + (y << 1) + z # A Number dictating the type of vote
	# vote = (x & y) | (x & z) | (y & z) # tried a bit vote, but harder to implement
	return vote

def step_x(reg):
	r13 = int(reg, 2) >> 5 & 1
	r16 = int(reg, 2) >> 2 & 1
	r17 = int(reg, 2) >> 1 & 1
	r18 = int(reg, 2) >> 0 & 1
	t = r13 ^ r16 ^ r17 ^ r18
	new_reg = str(t) + reg[:-1]
	return new_reg

def step_y(reg):
	r20 = int(reg, 2) >> 1 & 1
	r21 = int(reg, 2) >> 0 & 1
	t = r20 ^ r21
	new_reg = str(t) + reg[:-1]
	return new_reg

def step_z(reg):
	r7 = int(reg, 2) >> 15 & 1
	r20 = int(reg, 2) >> 2 & 1
	r21 = int(reg, 2) >> 1 & 1
	r22 = int(reg, 2) >> 0 & 1
	t = r7 ^ r20 ^ r21 ^ r22
	new_reg = str(t) + reg[:-1]
	return new_reg

def next_bit(key_x, key_y, key_z):
	x = int(key_x, 2) >> 0 & 1
	y = int(key_y, 2) >> 0 & 1
	z = int(key_z, 2) >> 0 & 1
	new_bit = x ^ y ^ z
	return new_bit

def string_to_binary(str):
	binary = ''
	for c in str:
		binary = binary + bin(ord(c))[2:].zfill(8)
	return binary

# Process Command Line Arguments
def entrypoint():
	parser = ArgumentParser(description='Software Implmentation of the A5/1 Stream Cipher')
	parser.add_argument('plaintext', nargs='?', default='plaintext')
	parser.add_argument('key', help='a 64-bit binary key used for generating the keystream', nargs='?', default='0000000000000000000000000000000000000000000000000000000000000000')
	args = parser.parse_args()
	
	original = args.plaintext

	print("Encrypting...")
	ciphertext = main(args)
	args.plaintext = ciphertext

	print("")
	print("Testing Results...")
	test = main(args)

	print("")
	print("Test Result: ", test == original)

# Runs Entrypoint to do Argument Parsing
if __name__ == "__main__":
    entrypoint()