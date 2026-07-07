public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int result = 0;
        for (int left = 0; left < num.Length; left++) {
            for (int right = 0; right < num.length; right++) {
                result = result * nums[right];
            }
            res[left] = result
        }
        return res
    }
}
