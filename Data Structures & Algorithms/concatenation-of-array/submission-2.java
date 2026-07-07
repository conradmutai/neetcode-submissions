class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] nums_out = new int[nums.size() * 2];
        
        for(int i = 0; i < nums.size() * 2; i++) {
            int j = 0;
            if (j == len(nums) - 1) {
                j = 0;
            }

            nums_out[i] = nums[j];
        }
    }
}