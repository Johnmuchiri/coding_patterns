import sys


def common_characters(arr):
    frequencies = [sys.maxsize for i in range(26)]
    common_chars = []
    for i in range(len(arr)):
        local_char_fred = [sys.maxsize for i in range(26)]
        for c in arr[i]:
            local_char_fred[ord(c) - ord("a")] += 1
        for i in range(26):
            frequencies[i] = min(frequencies[i], local_char_fred[i])
    for i in range(26):
        while frequencies[i] > 0:
            print(chr(ord(str(i)) + ord("a")))
            # common_chars.append(ord(str(i)) + ord("a"))
            frequencies[i] -= 1
    return common_chars


 print(common_characters(["bella", "label", "roller"]))
#
