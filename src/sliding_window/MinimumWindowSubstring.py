"""Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S."""


# naive approach


def find_min_window(s1, s2):
    end = 2

    key_word = [s2[i] for i in range(len(s2))]


    for i in range(len(s1)):
        if sorted(s2.lower()) ==sorted(s1[i:end]):

            pass




S = "ADOBECODEBANC"
T = "ABC"
find_min_window(S, T)
