#Bubble Sort
def __bubblesort__(arr):
    length= len(arr)
    
    for i in range(length):
        for j in range(0,length-i-1):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j]=arr[j],arr[j+1]

arr = [5,6,7,8,9,3]
print(arr)
__bubblesort__(arr)
print(arr)