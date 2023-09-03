# Array Sorting:
# Implement a Python function to sort an array of integers using the quicksort algorithm. 
#Include both the recursive and iterative versions of the algorithm.

### Using recursive call. 
def QS(arr):
    if len(arr) <= 1:
        return arr
    
    leftarr = []
    rightarr = []
    pivot = arr[0]

    for i in range(1,len(arr)):
        if pivot >= arr[i]:
            leftarr.append(arr[i])
        else:
            rightarr.append(arr[i])
    
    return QS(leftarr) +[pivot]  + QS(rightarr)

arr = [20,10,5,50,30,90,40]
print("Original array",arr)
sorted = QS(arr)
print("Sorted array",sorted)


#Iterative method has not been taught yet