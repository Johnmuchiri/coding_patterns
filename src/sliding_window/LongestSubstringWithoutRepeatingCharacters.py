"""Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring."""


##naive solution

def solution(s):

    store = []
    n = len(s)
    if n == 1:
        return s[0]
    for i in range(n):
        end_index = i
        seen_map = []
        for j in range(i, n - 1):
            if s[j] not in seen_map:
                end_index += 1
                seen_map.append(s[j])
            else:
                break
        store.append(len(s[i:end_index]))
    return max(store)


## sliding window approach

def solution_2(s):
    n = len(s)
    if n==0:
        return
    store = []
    start, end = 0, 0
    sum = 0
    seen_map = []

    for i in range(n):
        if s[i] not in seen_map:
            seen_map.append(s[i])
            end += 1
            sum += 1
            store.append(sum)
        else:
            sum -= 1
            start += 1
            seen_map.remove(s[start])

    return max(store)


class Solution:
    # @param A : string
    # @return an integer
    # @approach sliding window
    def lengthOfLongestSubstring(self, A):
        start = 0
        end = 0
        result = 0
        store = set()  ##{} set.add(), set.remove(item)
        sz = len(A)

        if len(A) == 1:
            return 1
        while start < sz and end < sz:
            if A[end] in store:
                store.remove(A[start])
                start += 1
            else:
                store.add(A[end])
                end += 1
                result = max(result, end - 1)

        return result


class Solution:
    # @param A : string
    # @return an integer
    # @approach sliding window
    def lengthOfLongestSubstring(self, A):
        i = j = result = 0

        sz = len(A)
        storage = set()

        while i < sz and j < sz:
            if A[j] in storage:
                storage.remove(A[i])
                i += 1
            else:
                storage.add(A[j])
                j += 1
                result = max(result, j - i)

        return result

# s = "bbbbb"
# s2 = "abcabcbb"
# print(solution(s2))
# print(solution_2(s2))

