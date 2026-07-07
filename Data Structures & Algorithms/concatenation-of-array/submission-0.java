class Solution {
    public int[] getConcatenation(int[] nums) {
        nums_out[len(nums) * 2];
        
        for(i = 0; i < len(nums) * 2; i++) {
            j = 0;
            if (j == len(nums) - 1) {
                j = 0;
            }

            nums_out[i] = nums[j];
        }
    }
}