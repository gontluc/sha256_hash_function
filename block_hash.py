from message_schedule import ms
from binary_addition import add
from functions import sigma0, sigma1
from compression import compress


def b_hash(block, pre_msg_sch):

    # Message schedule: 16 words of 32 bits
    msg_sch = ms(block)

    # Message schedule: 16 to 64 words
    t = 16
    while len(msg_sch) != 64:
        new_word = add([msg_sch[t-16], msg_sch[t-7], sigma1(msg_sch[t-2]), sigma0(msg_sch[t-15])])
        msg_sch.append(new_word)
        t += 1

    # Compression
    pre_msg_sch = compress(msg_sch, pre_msg_sch)

    return pre_msg_sch
