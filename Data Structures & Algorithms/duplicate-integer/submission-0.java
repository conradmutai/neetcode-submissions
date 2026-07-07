class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int i = 0; i < arr.length; i++) {
            for(int j = i + 1; j < arr.length; i++) {
                if(arr[i] == arr[j]) {
                    return true;
                }
            }
        }
    }
    return false;
}
