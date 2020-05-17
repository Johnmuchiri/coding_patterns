"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


##approach 1
def two_sum_1(arr, k):
    arr.sort()
    start = 0
    end = -1
    while start > end:
        sum = arr[start] + arr[end]
        if sum == k:
            return [arr[start], arr[end]]
        if sum > k:
            end -= 1
        if sum < k:
            start += 1
    return [-1, -1]


##approach2

def two_sum_2(arr, k):
    arr.sort
    store = []
    for i in range(len(arr)):
        diff = k - arr[i];
        if diff in store:
            return [arr[i], diff]
        else:
            store.append(arr[i])
    return [-1]


###3 some
def three_some(arr, k):
    two_some = []
    for i in range(len(arr)):
        two_some = two_sum_2(arr[1:], k - arr[i])
        if two_some[0] != -1:
            return two_some.append(arr[i])
    return [-1]

arr = [2, 7, 11, 15]
k = 9

print(three_some(arr, k))
