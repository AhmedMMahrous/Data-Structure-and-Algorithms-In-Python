arr = [[1,2,3],
       [4,5,6]]
print(arr)
print(len(arr))
print(len(arr[0]))

n = len(arr)
m = len(arr[0])
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')

print(arr[1][2])
