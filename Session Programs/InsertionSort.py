#Insertion Sort
def __insertionsort__(arr):
    
    for i in range(1,len(arr)):
        k = arr[i]
        j=i-1
        
        while(j>=0 and k<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=k

arr = [5,6,7,8,9,3]
print(arr)
__insertionsort__(arr)
print(arr)

