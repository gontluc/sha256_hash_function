def ch(w1, w2, w3):
    new_msg_32 = ""
    for bit in range(32):
        if w1[bit] == "1":
            new_msg_32 += w2[bit]
        else:
            new_msg_32 += w3[bit]
    return new_msg_32
