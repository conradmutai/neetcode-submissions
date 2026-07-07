from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_map = defaultdict(int)
        result = [] 

        for i in nums:
            num_map[tuple(nums)].append[i]

        for value in range(i+1, len(nums)):
            product = num_map.get(value)
            result.append(product)
