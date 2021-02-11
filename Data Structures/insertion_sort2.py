# Insertion sort implementation

arr = [32,1,23,55,34]

def insertion_sort():
    for i in range(1,len(arr)):
        temp = arr[i]
        hole = i
        while hole>0 and arr[hole - 1]> arr[hole]:
            arr[hole] = arr[hole-1]
            hole -=1
        arr[hole] = temp 

    print('Sorted array:{}'.format(arr))

insertion_sort()
       
