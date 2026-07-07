public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> num_map = new Dictionary<int, int>

        foreach (int num in nums) {
            int calculation = target - nums[i];

            if (num_map.ContainsKey(calculation)) {
                return new int[] {num_map[calculation], i};
            }

            num_map[nums[i]] = i;

        }

        return new int[] {;}
    }
}
