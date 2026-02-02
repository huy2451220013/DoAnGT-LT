class Solution(object):
    def destCity(self, paths):
        start = {i for i, j in paths}
        for i, j in paths:
            if j not in start:
                return j
