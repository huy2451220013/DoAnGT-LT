class Solution(object):
    def countEven(self, num):
        count = 0
        for i in range(1, num + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            if digit_sum % 2 == 0:
                count += 1
        return count