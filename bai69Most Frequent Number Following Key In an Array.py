from collections import defaultdict

class Solution:
    def mostFrequent(self, nums, key):
        freq = defaultdict(int)

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                freq[target] += 1
        return max(freq, key=freq.get)
sol = Solution()
print(sol.mostFrequent([1, 100, 200, 1, 100], 1))  
