public class Solution {
    public bool IsPalindrome(string s) {
        int left = 0;
        int right = s.Length - 1;

        while (left < right) {
            while (left < right && !alphaNum(s)) {
                left++;
            }
            while (right > left && !alphaNum(s)) {
                right--;
            }

            if (char.ToLower(s[left]) != char.ToLower(s[right])) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    public bool AlphaNum(char c) {
        return (c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z' || c >= '0' && c <= '9')
    }
}
