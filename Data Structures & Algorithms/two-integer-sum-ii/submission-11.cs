public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int left = 0; int right = numbers.Length;

        for(int i = 0; i < numbers.Length; i++) {
            int sum = nums[left] + nums[right];

            if (sum == target) {
                return {left + 1, right + 1};
            } else if (sum > target) {
                right--;
            } else {
                left++;
            }

        }

        return new int[0];
    }
}
