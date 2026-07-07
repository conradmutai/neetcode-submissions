class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = s.lower()
        right = (len(s) - 1)
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right < left and not self.alphaNum(s[right]):
                right += 1
            if s[left] != s[right]:
                return False

            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))