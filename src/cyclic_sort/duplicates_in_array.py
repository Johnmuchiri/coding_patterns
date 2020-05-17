from typing import List

"""
442. Find All Duplicates in an Array
Medium

1812

142

Add to List

Share
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup_store = []

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                dup_store.append(nums[i])

        return dup_store

