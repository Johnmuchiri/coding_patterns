from typing import List

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums):
            num = nums[start]
            if num < len(nums) and num != start:
                nums[num], nums[start] = nums[start], nums[num]
            else:
                start += 1
        print(nums)

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
