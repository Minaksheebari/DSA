# Array Rotation:
# Given an array of integers, write a Python function to rotate the array to the right by a given number of positions. Optimize the algorithm to have a time complexity of O(n).

### Using internet sources
def rotate_array(arr, k):
    n = len(arr)
    
    # Handle cases where k is greater than the length of the array
    k = k % n
    
    # Create a new list to store the rotated elements
    rotated_arr = []
    
    # Copy the last k elements to the new list
    for i in range(n - k, n):
        rotated_arr.append(arr[i])
    
    # Copy the first n-k elements to the new list
    for i in range(n - k):
        rotated_arr.append(arr[i])
    
    # Update the original array with the rotated elements
    for i in range(n):
        arr[i] = rotated_arr[i]

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr, 3)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
