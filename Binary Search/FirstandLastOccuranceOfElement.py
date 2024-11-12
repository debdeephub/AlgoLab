# class Solution:
#     def searchRange(self, nums, target):
#         left, right = 0, len(nums) - 1
#         first, last = -1, -1
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 first = mid
#                 last = mid
#                 while first > 0 and nums[first - 1] == target:
#                     first -= 1
#                 while last < len(nums) - 1 and nums[last + 1] == target:
#                     last += 1
#                 return [first, last]
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1        
#         return [first, last]


class Solution:
    def searchRange(self, nums, target):
        
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
        
        return [left, right]
            


arr = [ 2,4, 10, 10, 10, 18, 20]
target = 10

print(Solution().searchRange(arr, target))