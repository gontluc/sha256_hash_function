# sha256_hash_function

SHA256 Hash function

@gontluc november 2021

Main file: **sha256.py**

<br/>

![sha256 image](images/sha256-image.svg)

<br/>

---

OBJECTIVE: Build hash function Sha256.

---

<br/>

STEPS OF SHA256:

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

<br/>

---

DESCRIPTION OF THE OUTPUT: It displays almost every step in the terminal.

---

<br/>

OBSERVATIONS:

* It does not work with accents and other characters like "ñ".

* Probably has some other issues similar to the previous one that I have not encountered.

* First ever finished project in python.

* Good learning experience.

* Here is a [video](https://www.youtube.com/watch?v=f9EbD6iY9zI&ab_channel=learnmeabitcoin) of a good explanation of the steps of SHA256.
