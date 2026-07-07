public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] res = new int[n];
        int result = 0;
        for (int left = 0; left < n; left++) {
            for (int right = 0; right < n; right++) {
                result = result * nums[right];
            }
            res[left] = result;
        }
        return res;
    }
}
