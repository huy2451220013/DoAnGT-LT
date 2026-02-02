class Solution(object):
    def areOccurrencesEqual(self, s):
        return len(set([s.count(s1) for s1 in set(list(s))])) == 1
