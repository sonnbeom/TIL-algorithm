t = int(input())
for testCase in range(t):

    length = int(input())
    arr = list(map(int, input().split()))
    maxCount = 0

    for i in range(length - 1):
        tempMax = length - 1 - i
        for j in range(i+1, length):
            if arr[i] <= arr[j]:
                tempMax -= 1
        if tempMax > maxCount:
            maxCount = tempMax

    print(f'#{testCase} {maxCount}')
