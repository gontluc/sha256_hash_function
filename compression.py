from functions import eps0, eps1
from choice import ch
from binary_addition import add
from majority import maj


def compress(msg_sch, pre_msg_sch):

    # First 64 prime constants: prime**(1/3)
    k = ['01000010100010100010111110011000', '01110001001101110100010010010001',
         '10110101110000001111101111001111', '11101001101101011101101110100101',
         '00111001010101101100001001011011', '01011001111100010001000111110001',
         '10010010001111111000001010100100', '10101011000111000101111011010101',
         '11011000000001111010101010011000', '00010010100000110101101100000001',
         '00100100001100011000010110111110', '01010101000011000111110111000011',
         '01110010101111100101110101110100', '10000000110111101011000111111110',
         '10011011110111000000011010100111', '11000001100110111111000101110100',
         '11100100100110110110100111000001', '11101111101111100100011110000110',
         '00001111110000011001110111000110', '00100100000011001010000111001100',
         '00101101111010010010110001101111', '01001010011101001000010010101010',
         '01011100101100001010100111011100', '01110110111110011000100011011010',
         '10011000001111100101000101010010', '10101000001100011100011001101101',
         '10110000000000110010011111001000', '10111111010110010111111111000111',
         '11000110111000000000101111110011', '11010101101001111001000101000111',
         '00000110110010100110001101010001', '00010100001010010010100101100111',
         '00100111101101110000101010000101', '00101110000110110010000100111000',
         '01001101001011000110110111111100', '01010011001110000000110100010011',
         '01100101000010100111001101010100', '01110110011010100000101010111011',
         '10000001110000101100100100101110', '10010010011100100010110010000101',
         '10100010101111111110100010100001', '10101000000110100110011001001011',
         '11000010010010111000101101110000', '11000111011011000101000110100011',
         '11010001100100101110100000011001', '11010110100110010000011000100100',
         '11110100000011100011010110000101', '00010000011010101010000001110000',
         '00011001101001001100000100010110', '00011110001101110110110000001000',
         '00100111010010000111011101001100', '00110100101100001011110010110101',
         '00111001000111000000110010110011', '01001110110110001010101001001010',
         '01011011100111001100101001001111', '01101000001011100110111111110011',
         '01110100100011111000001011101110', '01111000101001010110001101101111',
         '10000100110010000111100000010100', '10001100110001110000001000001000',
         '10010000101111101111111111111010', '10100100010100000110110011101011',
         '10111110111110011010001111110111', '11000110011100010111100011110010']

    initial = pre_msg_sch.copy()

    # Compression
    n = 0
    for i in msg_sch:
        t1 = add([eps1(pre_msg_sch[4]), ch(pre_msg_sch[4], pre_msg_sch[5], pre_msg_sch[6]), pre_msg_sch[7], k[n], i])
        t2 = add([eps0(pre_msg_sch[0]), maj(pre_msg_sch[0], pre_msg_sch[1], pre_msg_sch[2])])
        pre_msg_sch.insert(0, add([t1, t2]))
        pre_msg_sch.pop()
        pre_msg_sch[4] = add([pre_msg_sch[4], t1])
        n += 1

    # initial + final
    result = []
    for i in pre_msg_sch:
        word = add([initial[pre_msg_sch.index(i)], i])
        result.append(word)

    return result
