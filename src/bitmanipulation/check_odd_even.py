"""
An integer is odd if and only if the least significant bit (LSB) is 1. By using AND (&) operator between given number
(num) and 1, we are eliminating all bits other than LSB. After this operation, if the result is 0,
that means LSB is 0 and the number is even. Otherwise, it is odd.
"""


def check_oddoreven(num):
    if (num & 1) == 0:
        print(f"Interger {num} is even")
    else:
        print(f"Interger {num} is odd")


# check_oddoreven(12)

def singleNumber(A):
    result =0
    bits_map = [0 for _ in range(32)]
    for i in range(32):
        for a in A:
            bits_map[i] += i >> 1 & 1
            bits_map[i] %= 3
    for i in range(32):
        result !=(bits_map[i]>>1)

    return result


A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
singleNumber(A)
