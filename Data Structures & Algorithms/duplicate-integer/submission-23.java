class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dupMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int val = nums[i];

            if(!dupMap.containsKey(val)) {
                dupMap.put(val, 1);
            } else {
                return true;
            }
        }

        return false;
    }
}