class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) + 1
        res = 0

        while left < right:
            currentSum = numbers[first] + numbers[last]

            if currentSum < target: 
                r -= 1
            if currentSum > target:
                l += 1
            if currentSum == target:
                return [l+1, r-1]
            
        