def longest_common_substring(s1, s2):
    cache = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_count = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0 and j == 0:
                cache[i][j] == 0
            elif s1[i] == s2[j]:
                cache[i][j] = cache[i - 1][j - 1] + 1
                max_count = max(cache[i][j], max_count)
            else:
                cache[i][j] == 0

    for i in range(len(cache)):
        print(cache[i])

    print(max_count)
    if max_count == 0:
        return 0

    i = 0
    j = 0

    lcs_w = [0 for i in range(max_count)]

    while cache[i][j] != 0:
        max_count -= 1
        lcs_w[max_count] = s1[i - 1]
        print("sss", s1[i - 1])

        i -= 1
        j -= 1

    print(lcs_w)


X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'

longest_common_substring(X, Y)
