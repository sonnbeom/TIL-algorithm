t = int(input())
for testCase in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    maxCount = 0
    minCount = arr[0]
    for i in range(n):
        if arr[i] > maxCount:
            maxCount = arr[i]
        if arr[i] < minCount:
            minCount = arr[i]
    print(f'#{testCase} {maxCount - minCount}')