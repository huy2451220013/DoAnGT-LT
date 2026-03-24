class Solution(object):
    def maxArea(self, height):
        left, right, max_area = 0, len(height) - 1, 0

        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1

        return max_area
        