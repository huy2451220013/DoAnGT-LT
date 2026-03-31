class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            if guess(1) == 0:
                return 1
            return 2
        i = (n + 1) // 2
        low = 1
        high = n
        while low <= high:
            a = guess(i)
            if a == 0:
                return i
            elif a < 0:
                high = i - 1
            else:
                low = i + 1
            i = (low + high) // 2
        return -1
