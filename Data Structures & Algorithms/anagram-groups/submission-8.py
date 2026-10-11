from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        res = []

        for st in strs:
            sorted_st = tuple(sorted(st))
            anagram_map[sorted_st].append(st)
        
        for val in anagram_map.values():
            res.append(val)

        return res