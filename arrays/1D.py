arr = [1,2,3,4]
print(len(arr))
arr.append(5)
print(len(arr))
print(arr)
for i in range(len(arr)):
    print(arr[i])

arr.pop()
print(arr)
arr.append(6)
print(arr)