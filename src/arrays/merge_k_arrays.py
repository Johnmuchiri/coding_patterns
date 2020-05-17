import heapq


def mergeK(arrs):
    heap = []
    for i in range(len(arrs)):
        heap.append((arrs[i][0], i, 0))
    heapq.heapify(heap)

    res = []
    while heap:
        val, index_arr, index_elem = heapq.heappop(heap)
        res.append(val)
        if index_elem + 1 < len(arrs[index_arr]):
            heapq.heappush(heap, (arrs[index_arr][index_elem + 1], index_arr, index_elem + 1))

    return res


arrayOfArrays = [[1, 5, 7, 11], [2, 3, 4, 8, 9], [3, 6, 9, 12, 15, 20]]
print(mergeK(arrayOfArrays))
