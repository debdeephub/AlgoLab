class Solution:
    def reverseBinarySearch(self,arr,key):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                end = mid - 1
            else:
                start = mid + 1




arr = [ 20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
key = 15

print(Solution().reverseBinarySearch(arr,key))