"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


def lps_n(s):
    start = 0
    end = 0
    for i in range(len(s)):
        even = expand_from_middle(s, i, i)
        odd = expand_from_middle(s, i, i + 1)
        ln = max(even, odd)
        if ln > (end - start):
            start = i - ((ln - 1) // 2)
            end = i + (ln // 2)

    return s[start:end]


def expand_from_middle(s, left, right):
    if s is None or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
