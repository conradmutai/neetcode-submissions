class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = 0

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum < target: 
                left += 1
            if currentSum > target:
                print(right)
                right -= 1
            if currentSum == target:
                return [left+1, right-1]
        return []
        