class Solution(object):
    def minimumSum(self, num):
        nums = sorted([num / 1000, num / 100 % 10, num / 10 % 10, num % 10])

        return (nums[0] * 10 + nums[3]) + (nums[1] * 10 + nums[2])