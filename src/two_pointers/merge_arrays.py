def merge_arrays(r1, r2):
    i = len(r1) - 1
    j = len(r2) - 1
    merge_index = len(r1) - 1

    while i >= 0 and j >= 0:
        if r1[i] > r2[j]:
            r1[merge_index] = r1[i]
            i -= 1
        else:
            r1[merge_index] = r2[j]
            j -= 1

        merge_index -= 1

    while j >= 0:
        r1[merge_index] = r2
        j -= 1
        merge_index -= 1
