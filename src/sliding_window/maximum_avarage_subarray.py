"""Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example:

Input: [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75"""
from _ast import List

"""Naive approach"""


def find_max_avarage(arr, k):
    n = len(arr)
    max_avarage = 0.0
    for i in range(n - k + 1):
        sum = 0.0
        for j in range(i, i + k):
            sum += arr[j]
        avarage_at_i = sum / 4
        max_avarage = max(avarage_at_i, max_avarage)

        if len(arr) == 1:
            return avarage_at_i

    return max_avarage


##sliding window approach

def find_max_avarage_2(arr, k):
    n = len(arr)
    avarage = []
    sum, start = 0, 0

    for i in range(n):
        sum += arr[i]
        if i >= k - 1:
            avarage.append(sum / k)
            sum -= arr[start]
            start += 1
    return max(avarage)


##approach2

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avarage = []
        sum, start = 0, 0
        for end in range(len(nums)):
            sum = sum + nums[end]
            if end >= k - 1:
                max_avarage.append(sum / k)
                sum = sum - nums[start]
                start += 1
        return max(max_avarage)


arr = [1, 12, -5, -6, 50, 3]
k = 4
# print(find_max_avarage(arr, 4))
print(find_max_avarage_2(arr, 4))
