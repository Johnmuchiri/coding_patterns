def longest_palidromic_subsequence(string):
    return lps_recursive(string, 0, len(string) - 1)


def lps_recursive(string, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if string[start] == string[end]:
        return 2 + lps_recursive(string, start + 1, end - 1)
    subsequence1 = lps_recursive(string, start + 1, end)
    subsequence2 = lps_recursive(string, start, end - 1)

    return max(subsequence1, subsequence2)


# string = "cbbd"##"bbbab"
# print(longest_palidromic_subsequence(string))


def _lps_dp(s, start, end, mem):
    if start > end:
        return 0

    if start == end:
        return 1

    if mem[start][end] == -1:

        if s[start] == s[end]:
            mem[start][end] = 2 + _lps_dp(s, start + 1, end - 1, mem)

        sub = _lps_dp(s, start + 1, end, mem)
        sub2 = _lps_dp(s, start, end - 1, mem)
        mem[start][end] = max(sub, sub2)

    return mem[start][end]


def longest_palidromic_subsequence_dp_topdown(s):
    mem = [[-1 for _ in range(len(s))] for _ in range(len(s))]

    return _lps_dp(s, 0, len(s) - 1, mem)


string = "bbbab"
print(longest_palidromic_subsequence_dp_topdown(string))