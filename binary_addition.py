from str_bin import str_to_bin
from pad_len_msg import pad_len


def add(list_to_add):
    integer_sum = 0
    for i in list_to_add:
        integer_sum += int(str_to_bin(i), 2)
    output = integer_sum % 2 ** 32
    to_bin = bin(output)
    to_str = to_bin[2:]
    result = pad_len(to_str, 32)
    return result
