class Solution:
    def countElements(self, nums, target):
        
        def binary_search(nums, target, firstOccFlag):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if firstOccFlag:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return right - left + 1
            


arr = [ 2,4, 10, 10, 10, 18, 20]
target = 10

print(Solution().countElements(arr, target))