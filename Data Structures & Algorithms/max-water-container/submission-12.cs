public class Solution {
    public int MaxArea(int[] heights) {
        int left = 0; int right = heights.Length - 1;
        int max_area = 0;

        while (left < right) {
            int width = right - left;
            int height = Math.Min(heights[left], heights[right]);
            int area = height * width;

            max_area = Math.Max(max_area, area);

            if (heights[left] < heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return max_area;
    }
}
