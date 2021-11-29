def separate(msg, bits):
    blocks = []
    word_block = ""
    counter = 0
    for i in msg:
        word_block += i
        counter += 1
        if counter == bits:
            counter = 0
            blocks.append(word_block)
            word_block = ""
    if word_block != "":
        blocks.append(word_block)
    return blocks
