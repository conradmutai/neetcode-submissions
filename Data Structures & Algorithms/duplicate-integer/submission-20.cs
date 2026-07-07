public class Solution {
    public bool hasDuplicate(int[] nums) {
        Dictionary<int, int> num_map = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++):
            if (num_map[nums[i]] < 2 && num_map[nums[i]] > 0):
                return True;
            else:
                return False;
            num_map.Add(nums[i], 0)
    }
}