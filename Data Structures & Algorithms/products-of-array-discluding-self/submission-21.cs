public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] res = new int[n];
    
        for (int left = 0; left < n; left++) {
            int result = 1;
            for (int right = 0; right < n; right++) {
                result = result * nums[right];
            }
            res[left] = result;
        }
        return res;
    }
}
