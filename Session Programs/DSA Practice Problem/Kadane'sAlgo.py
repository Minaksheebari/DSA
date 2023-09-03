# Given an array of integers, write a Python function to find the maximum subarray sum 
# (the sum of a contiguous subarray) using the Kadane's algorithm. 
# Provide the start and end indices of the subarray as well.

def kadane_max_subarray(arr):
    if not arr:
        return 0, 0, 0  # If the array is empty, return 0 sum and indices

    max_sum = arr[0]
    current_sum = arr[0]
    start_index = end_index = 0
    temp_start_index = 0

    for i in range(1, len(arr)):
        if arr[i] > (current_sum + arr[i]):
            current_sum = arr[i]
            temp_start_index = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

    return max_sum, start_index, end_index

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start_index, end_index = kadane_max_subarray(arr)
print("Maximum Subarray Sum:", max_sum)
print("Start Index:", start_index)
print("End Index:", end_index)
