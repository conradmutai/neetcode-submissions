class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        max_count, count = 0, 0
        
        while right < len(s):
            if s[right] != s[left]:
                count += 1
                max_count = max(max_count, count) 
            else:
                left = right
            right += 1
        return max_count  