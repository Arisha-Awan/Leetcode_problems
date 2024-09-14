from itertools import groupby

# 2419. Longest Subarray With Maximum Bitwise AND

# def max_sub(arr:list)->int:
#     max_bitwise=0
#     n=len(arr)
#     for i in range(n):
#         count=1
#         current_bitwise=arr[i]


#         for j in range(i+1,n):
#             count+=1
#             current_bitwise=current_bitwise & arr[j]
#             if current_bitwise==0:
#                 break
#             if current_bitwise>max_bitwise:
#                 max_bitwise=current_bitwise
#                 max_len=count
#         if current_bitwise>max_bitwise:
#                 max_bitwise=current_bitwise
#                 max_len=count
#     return max_len

# approach 2

# def max_sub(arr: list) -> int:
#     max_element = max(arr)
#     n = len(arr)
#     prev = arr[0]
#     count = 1
#     for i in range(1, n):
#         if arr[i] == max_element and arr[i] == prev:
#             count += 1
#         prev = arr[i]
#     return count


def longestSubarray(nums: list[int]) -> int:

    _max = max(nums)

    return max(
        (len(list(group)) for key, group in groupby(nums) if key == _max), default=0
    )


def max_sub(arr: list) -> int:
    max_element = max(arr)
    n = len(arr)
    prev = arr[0]
    count = 1
    max_count = 0
    for i in range(1, n):
        if arr[i] == max_element and arr[i] == prev:
            count += 1
        else:
            count = 1
        prev = arr[i]
        max_count = max(count, max_count)
    print(max_count)


# def longestSubarray(nums: list[int]) -> int:
#     _max = max(nums)
#     result, current_result = 0, 0
#     for n in nums:
#         if n == _max:
#             current_result += 1
#         else:
#             current_result = 0
#         result = max(result, current_result)
#     return result


nums = [1, 2, 3, 3, 2, 3, 3]

print(f"the maximum subarray bitwise and is:{longestSubarray(nums)}")

nums = [1, 2, 3, 4]
print(f"the maximum subarray bitwise and is:{longestSubarray(nums)}")
