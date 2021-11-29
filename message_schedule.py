def ms(block):
    n = 0
    word = ""
    words = []
    for bit in block:
        word += bit
        n += 1
        if n == 32:
            n = 0
            words.append(word)
            word = ""
    return words
