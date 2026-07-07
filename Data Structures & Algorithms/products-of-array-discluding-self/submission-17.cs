public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int res = int[]{};
        int result = 0;
        for (int left = 0; left < nums.Length; left++) {
            for (int right = 0; right < nums.length; right++) {
                result = result * nums[right];
            }
            res[left] = result;
        }
        return res;
    }
}
