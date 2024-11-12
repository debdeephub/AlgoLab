


def findFloorCeil(arr, n, x):
    low = 0
    high = n - 1
    ansFloor = -1
    ansCeil = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ansCeil = arr[mid]
            # look for smaller index on the left
            high = mid - 1
        else:
            ansFloor = arr[mid]
            low = mid + 1  # look on the right

    return [ansFloor,ansCeil]




arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = findFloorCeil(arr, n, x)
print(ans)
