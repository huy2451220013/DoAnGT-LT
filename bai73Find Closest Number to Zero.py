class Solution(object):
    def findClosestNumber(self, nums):
        mini=nums[0]
        for num in nums:
            if abs(num)<abs(mini):
                mini=num
            elif abs(num)==abs(mini):
                mini=max(num,mini)
        return mini
        
