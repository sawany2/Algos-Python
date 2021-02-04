# Selection Sort algorithm
#Time complexity: O(n^2)

arr = [12,33,2,5,56,32,34]

for i in range(0, len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[min],arr[i] = arr[i], arr[min]

print('Sorted array:{}'.format(arr))
