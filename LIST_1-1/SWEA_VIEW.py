for testCase in range(1,11):

    def bubbleSort(arr, n):
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr[0]

    houseCount = int(input())
    arr = list(map(int, input().split()))
    res = 0
    # n = 10 i = 9까지 8
    for i in range(2, houseCount - 2):
        if arr[i] > arr[i - 1] and arr[i] > arr[i - 2] and arr[i] > arr[i + 1] and arr[i] > arr[i + 2]:
            temp = 0
            lT = arr[i] - arr[i - 2]
            lO = arr[i] - arr[i - 1]
            rO = arr[i] - arr[i + 1]
            rT = arr[i] - arr[i + 2]
            listReq = [lT, lO, rO, rT]
            minDiff = bubbleSort(listReq, 4)
            res += minDiff
    print(f'#{testCase} {res}')
