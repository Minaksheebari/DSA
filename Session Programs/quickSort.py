def quickSort(arr):
    
    larr=[]
    rarr=[]
    pi = arr[0]
    for i in range(arr[1],len(arr)):
        if(i<=pi):
            larr.append(arr[i])
        else:
            rarr.append(arr[i])
    #Recursive call
    return quickSort(larr)+[pi]+ quickSort(rarr)

arr = [5,4,1,6,8,2]
print(arr)
sorted = quickSort(arr)
print(arr)

