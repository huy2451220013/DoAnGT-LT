class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        p = 0
        for i in range(0, len(heights)):
            if expected[i] != heights[i]:
                p += 1
        return p
