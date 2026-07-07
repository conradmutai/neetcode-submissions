class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(len(nums)):
            j = i + 1 
            for j in range(len(nums)):
                proposed = nums[i] + nums[j]
                if proposed == target:
                    return [i, j]
                
        return false