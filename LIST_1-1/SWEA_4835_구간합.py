t = int(input())
for testCase in range(1, t+1):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    maxSum = 0
    minSum = 0
    for i in range(m):
        minSum += arr[i]
    for i in range(n-m+1):
        tempSum = 0
        for j in range(i, m+i):
            tempSum += arr[j]
        if tempSum > maxSum:
            maxSum = tempSum
        if tempSum < minSum:
            minSum = tempSum
    print(f'#{testCase} {maxSum - minSum}')
