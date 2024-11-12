def countRotations(arr, n): 
  
    low = 0
    high = n - 1
    while(low <= high): 
        mid = low + ((high - low) // 2) 
        prev = (mid - 1 + n) % n 
        next = (mid + 1) % n 
  
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]: 
            return mid 
        # take the unsorted half
        elif (arr[mid] <= arr[high]): 
            high = mid - 1
        elif (arr[mid] >= arr[low]): 
            low = mid + 1
    return -1

# Driver code 
if __name__ == '__main__': 
    #arr = [8, 10, 12, 15, 18 ,2, 6] 
    #arr = [15, 18, 2, 3, 6, 12]
    #Clockwise Rotated
    #arr = [ 12, 15, 2, 6, 8, 12]
    #Anticlockwise Rotated
    #arr = [ 8, 10, 12, 15, 18, 2, 6]
    N = len(arr) 
    print(countRotations(arr, N)) 




# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         while (left < right):
#             mid = left + (right - left) // 2
#             if (nums[mid] < nums[right]):
#                 right = mid
#             elif (nums[mid] > nums[right]):
#                 left = mid + 1
#             else: 
#                 right -= 1
#         return nums[left]