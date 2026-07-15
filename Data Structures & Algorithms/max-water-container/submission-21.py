class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) - 1 
        max_area = 0
        
        while first < last:
            width = last - first
            height = min(heights[first], heights[last])
            current_area = width * height
            max_area = max(max_area, current_area)

            if heights[first] > heights[last]:
                last -= 1
            else:
                first += 1

        return max_area