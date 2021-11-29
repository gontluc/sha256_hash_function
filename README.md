# sha256_python_project
PyCharm Sha256 Project

@gontluc 12/11/2021

main file: sha256.py

---

OBJECTIVE: Build hash function Sha256 from the beginning.

---

STEPS OF Sha256:

1. Convert strings from the input data to binary.

2. Count number of blocks.

3. Separate in blocks of 512 bits.

4. Padding last two blocks.

5. Hash each block:
    1. Message schedule 16 words
    2. Message schedule 64 words
    3. Compression

6. Convert into hexadecimal

7. Concatenate

---

DESCRIPTION OF THE OUTPUT: It displays almost every step in the terminal, but it can be easily edited.

---

OBSERVATIONS:

-It does not work with accents and other characters like "ñ".

-Probably has some other issues similar to the previous that I have not encountered.

-First ever finished project in python.

-Good learning experience.

-Link to a explanation video:

https://www.youtube.com/watch?v=f9EbD6iY9zI&ab_channel=learnmeabitcoin
