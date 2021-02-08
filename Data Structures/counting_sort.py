
# Counting sort implementation



def counting_sort():
    #arr = [3,4,5,2,1,1,2,3,2,3,5]
    arr = [9,4, 1,7 ,9 ,1 ,2 , 0]
    import pdb

    count = [0] * (max(arr) + 1)

    print('Count array:{}'.format(count))

    for i in range(len(arr)):
        count[arr[i]] += 1


    print('Count array:{}'.format(count))


    
    for i in range(1, len(count)):
        count[i] = count[i-1] + count[i]

    pdb.set_trace()
    #print(list(range(10,0,-1)))
    for i in range(len(count)-1,0,-1):
        count[i] = count[i-1]

    print('Count array:{}'.format(count))

    sorted_array = [None ] * len(arr)

    for item in arr:
        sorted_array[count[item]] = item
        count[item]+=1

    print('Sorted array: {}'.format(sorted_array))     


counting_sort()

