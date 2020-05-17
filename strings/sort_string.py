"""
Given a string of lowercase characters from ‘a’ – ‘z’. We need to write a program to print the characters of this string in sorted order.

Examples:

Input : bbccdefbbaa
Output : aabbbbccdef

Input : geeksforgeeks
Output : eeeefggkkorss

"""


def sort_string(s1):
    if not s1:
        return ""
    char_arr = [0 for i in range(26)]
    for i in range(len(s1)):
        char_arr[ord(s1[i]) - ord('a')] += 1
    print(char_arr)
    ##print items
    res = ""
    for i in range(0, 26):

        for j in range(char_arr[i]):
            print(j)
            res += chr(ord('a') + i)

    return res


s1 = "geekforgeeks"
print(sort_string(s1))
