# Shell sort implementation
import math

#arr = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
arr = list(range(100,0,-1))
#gap = abs(len(arr)/2)
gap =3

while gap>0:
    i = 0
    while i< gap:
        for j in range(i+gap, len(arr),gap):
            temp = arr[j]
            hole = j
            while hole>0 and arr[hole-gap]>temp:
                arr[hole] = arr[hole-gap]
                hole = hole -gap
            arr[hole] = temp
        i +=1
    gap = math.floor(gap/2)


print('Sorted array:{}'.format(arr))