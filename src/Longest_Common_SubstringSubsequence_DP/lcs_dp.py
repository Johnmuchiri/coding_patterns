"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A common subsequence of two strings is a subsequence that is common to both strings. If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

"""


##Brute force solution 0(2^(N+M)) N&M equals to the
##length of the two strings, space complexity is 0(N+M)

def _lcs_recursive(text1: str, text2: str, i, j):
    if i == len(text1) or j == len(text2):
        return 0
    if text1[i] == text2[j]:
        return 1 + _lcs_recursive(text1, text2, i + 1, j + 1)
    return max(_lcs_recursive(text1, text2, i + 1, j), _lcs_recursive(text1, text2, i, j + 1))


def lcs_brute_force(text1: str, text2: str) -> int:
    return _lcs_recursive(text1, text2, 0, 0)


#
#
# text1 = "abc",
# text2 = "abc"
# print(lcs_brute_force(text1, text2))


"""
Top-down Dynamic Programming with MemoizationPermalink
We can use a two-dimensional array to store the already solved subproblems

Time Complexity: O(N * M) where N and M are the lengths of two input strings.

Space Complexity: O(N * M)

"""


def _lcs_dp_recursive(text1, text2, i, j, mem):
    if i == len(text1) or j == len(text2):
        mem[i][j] = 0
    if mem[i][j] == -1:
        if text1[i] == text2[j]:
            mem[i][j] = 1 + _lcs_dp_recursive(text1, text2, i + 1, j + 1, mem)
        else:
            mem[i][j] = max(_lcs_dp_recursive(text1, text2, i + 1, j, mem),
                            _lcs_dp_recursive(text1, text2, i, j + 1, mem))
    return mem[i][j]


def lcs_dp(text1, text2):

    memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

    return _lcs_dp_recursive(text1, text2, 0, 0, memo)


text1 = "abc",
text2 = "abc"
print(lcs_dp(text1, text2))
