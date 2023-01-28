def countingSort(arr):
    ans = []
    for i in range(100):
        ans.append(0)
    for j in arr:
        ans[j] += 1
    return ans
