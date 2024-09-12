def searchMatrix(matrix: int, target: int):
    def target_row(rows: int, target: int):
        i = 0
        while i < rows:
            if matrix[i][0] > target:
                break
            i += 1
        return i

    rows = len(matrix)
    cols = len(matrix[0])
    targeted_row = target_row(rows, target)
    if targeted_row == 0:
        return False
    for j in range(cols):
        if matrix[targeted_row - 1][j] == target:
            return True

    return False


# Test cases
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

# Example 1
print(searchMatrix(matrix, 3))  # Expected output: True

# Example 2
print(searchMatrix(matrix, 13))  # Expected output: False

# Additional Test Case
print(searchMatrix(matrix, 1))  # Expected output: True
print(searchMatrix(matrix, 60))  # Expected output: True
print(searchMatrix(matrix, 0))  # Expected output: False
