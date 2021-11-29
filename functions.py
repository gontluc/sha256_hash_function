from exclusiveor import xor


def sigma0(msg_32):
    return xor(msg_32, 7, 18, 3, True)


def sigma1(msg_32):
    return xor(msg_32, 17, 19, 10, True)


def eps0(msg_32):
    return xor(msg_32, 2, 13, 22, False)


def eps1(msg_32):
    return xor(msg_32, 6, 11, 25, False)

