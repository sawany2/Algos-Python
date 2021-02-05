
# Quick Sort implementation

arr = list(range(200,-1,-1))
print(arr)

def partition(lb, ub):
    pivot = lb
    
    start,end = lb+1, ub

    while start < end:
        while arr[start]<= arr[pivot] and start < ub:
            start+=1
        while arr[end] > arr[pivot] and end > lb:
            end -=1

        if start < end:
            arr[start],arr[end]= arr[end],arr[start]
            start +=1
            end -=1
    
    arr[end],arr[pivot] = arr[pivot],arr[end]

    return end

def quick_sort(lb,ub):
    if lb<ub:
        loc = partition(lb,ub)
        quick_sort(lb,loc-1)
        quick_sort(loc+1,ub)


quick_sort(0,len(arr)-1)

print("Sorted Array:{}".format(arr))

    