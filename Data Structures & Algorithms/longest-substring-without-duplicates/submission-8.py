class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_map = {}
        left, right = 0, 1
        max_count, count = 0, 0
        
        while right in range(len(s)):
            if s[right] in string_map:
                left = max(string_map[s[right]] + 1, left)
            string_map[s[right]] = right
            max_count = max(max_count, right - left + 1)
        return max_count  