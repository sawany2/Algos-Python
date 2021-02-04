# Insertion Sort

arr = list(range(100,-1,-1))
print('Original Array:{}'.format(arr))

for i in range(1,len(arr)):
    j = i-1
    temp = arr[i]
    while j >-1 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1]=temp

print('Sorted Array:{}'.format(arr))
