def search_matrix(arr, t):
    row = 0
    col = len(arr[0]) - 1

    while row <= len(arr) and col >= 0:
        if arr[row][col] == t:
            return True
        if arr[row][col] < t:
            row += 1
        if arr[row][col] > t:
            col -= 1
    return False
