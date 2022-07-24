def Bubble_Sort(arr):
    n = len(arr)
    pemitation = True
    while pemitation:
        pemitation = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i] 
                pemitation = True
            
arr = [10,5,6,7,9,6]
print(arr)
Bubble_Sort(arr)
print(arr)