class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length(); i++) {
            for(int j = 1; i < nums.length(); i++) {
                if(nums.getValue(i) + nums.getValue(j) == target) {
                    return("[" + i + "," + j + "]");
                }
            }
        }
    }
}
