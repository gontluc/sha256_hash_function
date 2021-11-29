def str_to_binary(msg):
    ascii_ord, binary_list = [], []
    binary_str = ""
    for i in msg:
        ascii_ord.append(ord(i))
    for i in ascii_ord:
        binary_list.append(bin(i)[2:])
    for i in binary_list:
        if len(i) != 8:
            binary_str += (8 - len(i)) * "0" + i
        else:
            binary_str += i
    return binary_str
