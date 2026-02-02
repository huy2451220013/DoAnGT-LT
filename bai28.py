from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        freq=Counter(stones)
        for jl in jewels:
            if jl in freq:
                count+=freq[jl]
        return count
        