""""This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)]"""


# def merge_intervals(arr):
#     merged_intervals_list = []
#
#     arr.sort(key=lambda x: x[0])
#     print(arr)
#
#     for i in range(0, len(arr), 2):
#         (c_start, c_end) = arr[i]
#         (n_start, n_end) = arr[i + 1]
#         new_start = c_start
#         new_end = n_end
#
#         if c_start <= n_start:
#             new_start = n_start
#             if c_end >= n_start:
#                 new_end = c_end
#
#         else:
#             new_end = c_end
#
#         print(new_start, new_end)
#
#         merged_intervals_list.append((new_start, new_end))
#
#     return merged_intervals_list
#
#
# arr = [(1, 3), (5, 8), (4, 10), (20, 25)]
# print(merge_intervals(arr))


def merge_intervals_a(arr):
    merged_intervals_list = []

    arr.sort(key=lambda x: x[0])

    for i in range(0, len(arr), 2):
        (c_start, c_end) = arr[i]
        (n_start, n_end) = arr[i + 1]
        merged_intervals_list.append((c_start, c_end))
        if n_end > c_end:
            merged_intervals_list.append((n_start, n_end))
        else:
            merged_intervals_list.append((c_start, n_end))

    return merged_intervals_list


def merge_intervals(arr):
    arr.sort(key=lambda x: x[0])
    stack = [arr[0]]
    for i in range(1, len(arr)):
        (s, e) = stack[-1]
        (start, end) = arr[i]
        if end > e:
            stack.append(arr[i])
        else:
            stack.pop()
            stack.append((s, end))

    return stack


arr = [(1, 3), (5, 8), (4, 10), (20, 25)]
# print(merge_intervals(arr))
print(merge_intervals_a(arr))

