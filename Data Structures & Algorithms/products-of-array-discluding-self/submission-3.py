class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_map = {}
        result = [] 

        for i in nums:
            num_map[i] = 1 + num_map.get(i, 0)

        for value in range(i+1, len(nums)):
            product = num_map.get(value)
            result.append(product)
