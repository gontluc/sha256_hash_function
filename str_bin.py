def str_to_bin(str_32):
    result = 0
    n = 1
    for bit in str_32:
        if bit == "1":
            result += 2**(32-n)
        n += 1
    return bin(result)
