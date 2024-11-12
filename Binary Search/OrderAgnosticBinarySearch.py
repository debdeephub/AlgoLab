class Solution:
    def orderAgnosticBinarySearch(self,arr,key):
        start = 0
        end = len(arr) - 1
        flag = "ascending"
        if arr[0] > arr[-1]:
            flag = "descending"
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key if flag == "ascending" else arr[mid] < key:
                end = mid - 1
            else:
                start = mid + 1
        return -1



arrDesc = [ 20, 17, 15, 14, 13, 12, 10, 9, 8, 4 ]
arrAsc = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 14, 15, 17, 20 ]
key = 14

print(Solution().orderAgnosticBinarySearch(arrDesc,key))

print(Solution().orderAgnosticBinarySearch(arrAsc,key))