"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

##O(n2) time complexity on space complexity

from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if not nums:
            return 0
        mem = [1 for i in range(len(nums))]
        mem[0] = 1
        for i in range(1, len(nums)):

            for j in range(0, i):
                if nums[i] >= nums[j] and mem[i] < mem[j] + 1:
                    mem[i] = mem[j] + 1

        print(mem)

        return max(mem)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
sol = Solution()
print(sol.lengthOfLIS(arr))
