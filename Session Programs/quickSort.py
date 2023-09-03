def quickSort(arr):
    if not arr:
        return []
    larr=[]
    rarr=[]
    pi = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]<=pi):
            larr.append(arr[i])
        else:
            rarr.append(arr[i])
    #Recursive call
    return quickSort(larr)+[pi]+ quickSort(rarr)

arr = [5,4,1,6,8,2]
print(arr)
sorted = quickSort(arr)
print(sorted)

