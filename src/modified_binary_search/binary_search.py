"""
Given a sorted (in ascending order) integer array nums of n elements and a target
 value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

"""


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            start = mid - 1
        if arr[mid] < target:
            start = mid+1
    return -1


print(400>>2)