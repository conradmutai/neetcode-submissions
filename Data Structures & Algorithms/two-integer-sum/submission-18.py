class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i+1 
            for j in range(len(nums)):
                proposed = num[i] + num[j]
                if proposed == target:
                    return [i, j]
                
        return false