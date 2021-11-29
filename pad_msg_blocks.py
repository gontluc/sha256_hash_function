def pad_blocks(unpad_blocks, unlucky_block, bits_remaining, len_msg):
    last_unlucky_block = "1" + ("0" * 447) + len_msg
    last_unlucky_block2 = ("0" * 448) + len_msg
    blocks = unpad_blocks.copy()

    if unlucky_block:
        if bits_remaining == 0:
            blocks.append(last_unlucky_block)
        else:
            blocks[-1] += "1" + ("0" * (512 - bits_remaining - 1))
            blocks.append(last_unlucky_block2)
    else:
        blocks[-1] += "1" + ("0"*(512-bits_remaining-64-1)) + len_msg

    return blocks
