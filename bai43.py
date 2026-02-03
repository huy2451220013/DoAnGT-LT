class Solution(object):
    def reformatNumber(self, number):
        digits = ''.join(c for c in number if c.isdigit())
        blocks = []
        n = len(digits)
        while n > 4:
            blocks.append(digits[:3])
            digits = digits[3:]
            n -= 3
        if n == 4:
            blocks.append(digits[:2])
            blocks.append(digits[2:])
        else:
            blocks.append(digits)
        return '-'.join(blocks)