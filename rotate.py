def rot(msg_32, n):
    new_msg_32 = ""
    for bit in msg_32[-n:]:
        new_msg_32 += bit
    for bit in msg_32[0:(32-n)]:
        new_msg_32 += bit
    return new_msg_32
