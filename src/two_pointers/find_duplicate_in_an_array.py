"""Find duplicate in an array

Note:  same as Find cycle in the linked list

"""


def find_duplicate(arr):
    slow_pointer = arr[0]
    fast_pointer = arr[0]

    fast_pointer = arr[arr[fast_pointer]]
    slow_pointer = arr[slow_pointer]

    while fast_pointer != slow_pointer:
        print(slow_pointer, fast_pointer)
        fast_pointer = arr[arr[fast_pointer]]
        slow_pointer = arr[slow_pointer]
    ##there is a n duplicate
    ##get the start of the cycle

    fast_pointer = arr[0]
    # cycle_val = 0
    while True:
        fast_pointer = arr[arr[fast_pointer]]
        fast_pointer = arr[slow_pointer]
        if fast_pointer == fast_pointer:
            cycle_val = slow_pointer
            break
    return cycle_val


arr = [1, 3, 4, 2, 2]
print(find_duplicate(arr))

# f = arr[0]
# s = arr[0]
# print(s, f)
# f = arr[arr[f]]
# s = arr[s]
# print(s, f)
#
# f = arr[arr[f]]
# s = arr[s]
# print(s, f)



##test

# arr =[1, 2, 2, 3, 3, 4, 7, 8]
# k =0
# for i in range(len(arr)-1):
#     if arr[i] != arr[i+1]:
#         print(arr[i])
#         arr[k] = arr[i]
#         k+=1
#
# arr[k]=arr[-1]
#
# print(arr[:k+1])
