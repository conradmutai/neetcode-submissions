class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = s.replace(" ", "").lower()
        s = "".join(char for char in s if char.isalpha())
        right = (len(s) - 1)
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True