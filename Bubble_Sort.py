def countSwaps(a):
    cnt = 0
    n=len(a)
    tmp = 0
    for i in range(n):
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                tmp = a[j]
                a[j]=a[j + 1]
                a[j + 1] = tmp
                cnt +=1
    print("Array is sorted in {} swaps.".format(cnt))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
