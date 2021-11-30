from binary import str_to_binary
from block_counter import count_blocks
from separate_blocks import separate
from pad_len_msg import pad_len
from pad_msg_blocks import pad_blocks
from block_hash import b_hash


# Constants primeNumber**(1/2)
pre_msg_sch = ['01101010000010011110011001100111', '10111011011001111010111010000101',
               '00111100011011101111001101110010', '10100101010011111111010100111010',
               '01010001000011100101001001111111', '10011011000001010110100010001100',
               '00011111100000111101100110101011', '01011011111000001100110100011001']


# Input message
msg = "abc"


# Step 1: Convert strings from the input data to binary
binary_msg = str_to_binary(msg)
print("Step 1: Convert strings from the input data to binary")
print(binary_msg)
print()


# Step 2: Count number of blocks
tuple1 = count_blocks(binary_msg)
n_blocks = tuple1[0]
unlucky_block = tuple1[1]
bits_remaining = tuple1[2]
print(
      f"Step 2: Count number of blocks\n"
      f"    Number of blocks: {n_blocks+1}\n"
      f"    Bits remaining: {bits_remaining}"
)
print()


# Step 3: Separate in blocks of 512 bits
unpad_blocks = separate(binary_msg, 512)
print("Step 3: Separate in blocks of 512 bits")
print(unpad_blocks)
print()


# Step 4: Padding last two blocks
len_msg = bin(len(binary_msg))[2:]
len_msg = pad_len(len_msg, 64)
blocks = pad_blocks(unpad_blocks, unlucky_block, bits_remaining, len_msg)
print("Step 4: Padding last two blocks")
print(blocks)
print()


# Step 5: Hash each block
block_result = []
for block in blocks:
    block_result = b_hash(block, pre_msg_sch)
    pre_msg_sch = block_result


# Result of Step 5: Display final hash value of all blocks
print("Step 5: Final hash value (binary): ")
for i in block_result:
    print(i)
print()


# Step 6: Convert into hexadecimal
print("Step 6: Final hash value (hexadecimal): ")
hex_block = []
for i in block_result:
    hex_word = hex(int(i, 2))[2:]
    if len(hex_word) != 8:
        hex_word = "0"*(8-len(hex_word)) + hex_word
    hex_block.append(hex_word)
    print(hex_word)
print()


# Step 7: Concatenate
print("Step 7: Concatenate: ")
msg_digest = ""
for i in hex_block:
    msg_digest += i
print(msg_digest)
