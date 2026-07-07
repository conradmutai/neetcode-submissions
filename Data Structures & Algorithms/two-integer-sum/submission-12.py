class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in len(nums):
            j = j+1 
            for j in len(nums):
                proposed = num[i] + num[j]
                if proposed == target:
                    return [i, j]
                
        return false