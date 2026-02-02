class Solution(object):
    def thousandSeparator(self, n):
        num = str(n)
        if len(num) < 4: return num

        left = self.thousandSeparator(num[:(len(num) - 3)])
        right = num[(len(num) - 3):]

        return left + "." + right
        
