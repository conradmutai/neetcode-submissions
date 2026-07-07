class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) - 1 
        max_area = 0
        
        while first < last:
            width = last - first
            min_area = min(height[first], height[last])
            area = min_area * width

            max_area = max(max_area, area)

            if height[first] < height[last]:
                left += 1
            else:
                right -= 1

        return max_area 