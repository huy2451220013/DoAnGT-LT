class Solution(object):
    def findContentChildren(self, g, s):
        g.sort() 
        s.sort()
        contentChildren = 0
        i = 0 
        j = 0 
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                contentChildren += 1
                i += 1
            j += 1
        return contentChildren
