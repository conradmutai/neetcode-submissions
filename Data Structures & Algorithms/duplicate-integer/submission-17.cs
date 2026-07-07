public class Solution {
    public bool hasDuplicate(int[] nums) {
        Dictionary<int, int> num_map = new Dictionary<int, int>();
        for i in range(len(nums)):
            if (num_map[nums[i]] > 2 && num_map[nums[i]] > 0):
                return True;
            else:
                return False;
            num_map.add(nums[i])
    }
}