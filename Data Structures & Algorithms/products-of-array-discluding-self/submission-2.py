class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_map = {}
        result = [] 

        for i in nums:
            num_map[tuple(nums)].append[i]

        for value in range(i+1, len(nums)):
            product = num_map.get(value)
            result.append(product)
