def xorQueries(arr, queries):
    # Step 1: Build the prefix XOR array
    prefix_xor = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

    # Step 2: Answer each query using the prefix XOR array
    result = []
    for left, right in queries:
        xor_result = prefix_xor[right + 1] ^ prefix_xor[left]
        result.append(xor_result)

    return result


# Example usage
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
print(xorQueries(arr, queries))  # Output: [2, 7, 14, 8]
