class Solution(object):
    def distributeCandies(self, candies, num_people):
        n = num_people
        result = [0] * n
        c = 0
        while candies > 0:
            result[c % n] += min(candies, c+1)
            c += 1
            candies -= c
        return result