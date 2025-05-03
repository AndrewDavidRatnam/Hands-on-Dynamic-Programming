def maxSum(arr):
    length = len(arr)
    if length == 0:
        return 0 
    if length == 1:
        return arr[0]
    max_sum = [0]*length
    max_sum[0] = arr[0]
    max_sum[1] = max(arr[0], arr[1])

    for i in range(2,length):
        max_sum[i] = max(max_sum[i-1], (max_sum[i-2] + arr[i]) )
    return max_sum[-1]

for arr in [[5, 5, 10, 100, 10, 5], [3, 2, 5, 10, 7],[3, 2, 7, 10]]:

    print(f"Max sum of {arr} : {maxSum(arr)}")