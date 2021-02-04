# Bubble sort

arr = [15, 44, 24, 16, 6, 8, 5]

j = len(arr) - 1
while j > 0:
    i = 0
    flag = 0
    while i < j:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1]= arr[i+1], arr[i]
            flag = 1
        i += 1
    if flag == 0:
        break
    j -= 1

print('Sorted array:{}'.format(arr))