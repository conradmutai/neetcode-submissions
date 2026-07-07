import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)

        for num in nums:
            mid = first + ((last - first) // 2)

            if nums[mid] >= target:
                last = mid
            elif nums[mid] < target:
                first = mid + 1
        return l if (l < len(nums) and nums[l] == target) else -1
        
        
