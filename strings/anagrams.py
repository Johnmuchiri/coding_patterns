"""Given two strings, write a function to determine whether they are anagrams.


"""


def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    s1.lower()
    s2.lower()
    chars = [0 for i in range(256)]
    for i in range(len(s1)):
        chars[i] += 1
    for j in range():
        chars[j] -= 1

    for k in chars:
        if k != 0:
            return False

    return True
