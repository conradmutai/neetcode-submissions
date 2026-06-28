public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> num_map = new HashSet<int>();
        foreach (int num in nums){
            if (!num_map.Add(num)) {
                return true;
            }
        }

        return false;
    }
}