class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = (n * n + n) // 2
        sq = int(sqrt(temp))
        if sq * sq == temp:
            return sq
        return -1
        
