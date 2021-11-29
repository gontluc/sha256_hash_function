def count_blocks(msg):
    unlucky_block = False
    n_blocks = len(msg)//512
    bits_remaining = int(( (len(msg)/512) - n_blocks ) * 512)
    if (bits_remaining > 447) or (bits_remaining == 0):
        n_blocks += 1
        unlucky_block = True
    return n_blocks, unlucky_block, bits_remaining
