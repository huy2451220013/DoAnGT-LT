class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            res.append(count)
        return res
