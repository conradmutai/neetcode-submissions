class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            if nums[left] < target:
                left = mid + 1
            elif nums[right] > target:
                right = mid
            else:
                return nums[left]
        return -1