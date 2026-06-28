from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        res = 0 

        for num in nums:
            if not num_map[num]:
                num_map[num] = num_map[num-1] + num_map[num+1] + 1
                num_map[num - num_map[num-1]] = num_map[num]
                num_map[num + num_map[num+1]] = num_map[num]
                res = max(res, num_map[num])
        return res 