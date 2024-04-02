def deleteFromArray(arr,n,idx):
    #code here

    for i in range(idx, n - 1):
            arr[i] = arr[i + 1]
    arr[n - 1] = 0
    return arr  