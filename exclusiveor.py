from shift import shf
from rotate import rot


def xor(msg_32, r1, r2, r3, with_shf):
    word1 = rot(msg_32, r1)
    word2 = rot(msg_32, r2)
    if with_shf:
        word3 = shf(msg_32, r3)
    else:
        word3 = rot(msg_32, r3)

    new_msg_32 = ""

    for bit in range(32):
        if word1[bit] == word2[bit]:
            if word3[bit] == "1":
                new_msg_32 += "1"
            else:
                new_msg_32 += "0"
        else:
            if word3[bit] == "0":
                new_msg_32 += "1"
            else:
                new_msg_32 += "0"
    return new_msg_32
