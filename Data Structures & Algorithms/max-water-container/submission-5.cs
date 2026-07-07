public class Solution {
    public int MaxArea(int[] heights) {
        left = 0; right = heights.Length;

        while (left < right) {
            int width = right - left;
            int height = Math.min(heights[left], heights[right]);
            int area = height * width;

            int max_area;

            if (max_area > area) {
                max_area = max_area
            } else {
                max_area = area
            }
            
            if (heights[left] < heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return max_area;
    }
}
