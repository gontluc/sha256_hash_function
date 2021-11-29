def pad_len(len_msg, bits):
    if len(len_msg) != bits:
        len_msg = "0" * (bits - len(len_msg)) + len_msg
    return len_msg
