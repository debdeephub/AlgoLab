class Solution:
    def binarySearch(self,arr,key):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1


arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20]
key = 17

print(Solution().binarySearch(arr,key))