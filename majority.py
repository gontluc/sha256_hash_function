def maj(w1, w2, w3):
    new_msg_32 = ""
    for bit in range(32):
        if w1[bit] == "1":
            if (w2[bit] == "1") or (w3[bit] == "1"):
                new_msg_32 += "1"
            else:
                new_msg_32 += "0"
        else:
            if (w2[bit] == "0") or (w3[bit] == "0"):
                new_msg_32 += "0"
            else:
                new_msg_32 += "1"
    return new_msg_32
