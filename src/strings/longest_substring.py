class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
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
                print(store)

            else:
                sum -= 1
                start += 1
                # seen_map.pop(0)

        return max(store)