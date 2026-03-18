class Solution(object):
    def numberGame(self, nums):
        nums.sort(reverse = True)
        ans =[]
        n = len(nums)
        while nums:
            alice = nums.pop()
            bob = nums.pop()
            ans.append(bob)
            ans.append(alice)
        return ans