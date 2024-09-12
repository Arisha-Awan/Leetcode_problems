# def searchMatrix(matrix:int,target:int):
#     if not matrix:
#         return False

#     rows=len(matrix)
#     cols=len(matrix[0])
#     left=0
#     right=rows*cols-1
#     while left<=right:
#         mid=(left+right)//2
#         mid_row=mid//cols
#         mid_col=mid%cols
#         mid_value=matrix[mid_row][mid_col]
#         if mid_value==target:
#             return True
#         elif mid_value<target:
#             left=mid+1
#         else:
#             right=mid-1

#     return False


# # Test cases
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]

# # Example 1
# print(searchMatrix(matrix, 3))  # Expected output: True

# # # Example 2
# print(searchMatrix(matrix, 13)) # Expected output: False


# # # Additional Test Case
# print(searchMatrix(matrix, 1))  # Expected output: True
# print(searchMatrix(matrix, 60)) # Expected output: True
# print(searchMatrix(matrix, 0))  # Expected output: False
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # Find the row where the target might be located
    def target_row(rows: int, target: int) -> int:
        i = 0
        while i < rows:
            if matrix[i][0] > target:
                break
            i += 1
        return i

    rows = len(matrix)
    cols = len(matrix[0])

    # Find the row that could potentially contain the target
    targeted_row = target_row(rows, target)

    # If targeted_row is 0, it means the target is less than the smallest element in the matrix
    if targeted_row == 0:
        return False

    left = 0
    right = cols - 1
    row = targeted_row - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[row][mid]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test cases
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

# Example 1
print(searchMatrix(matrix, 3))  # Expected output: True

# Example 2
print(searchMatrix(matrix, 13))  # Expected output: False

# Additional Test Cases
print(searchMatrix(matrix, 1))  # Expected output: True
print(searchMatrix(matrix, 60))  # Expected output: True
print(searchMatrix(matrix, 0))  # Expected output: False
