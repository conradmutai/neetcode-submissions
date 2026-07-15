import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        

        while first <= last:
            middle = first + ((last - first) // 2)

            if nums[middle] == target:
                return middle
            else:
                if nums[middle] > target:
                    last = middle - 1
                elif nums[middle] < target:
                    first = middle + 1
            
        return -1

        
        
