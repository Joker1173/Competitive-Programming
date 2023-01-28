
def insertionSort1(n, arr):
    e = arr[-1]
    for i in range(n-2,-1,-1):
        if e < arr[i]:
            arr[i+1] = arr[i]
            print(" ".join(str(k) for k in arr))
        if arr[i] > e:
            arr[i] = e
    print(" ".join(str(k) for k in arr))
