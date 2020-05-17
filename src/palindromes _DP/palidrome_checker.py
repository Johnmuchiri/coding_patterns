def isPalindrome(s, i, j):
    l = i
    r = j
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

s ="aba"
print(isPalindrome(s, 0, len(s)-1))
