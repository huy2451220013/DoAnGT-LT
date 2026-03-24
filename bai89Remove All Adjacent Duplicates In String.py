class Solution(object):
    def removeDuplicates(self, s):
        self.stack = []

        for char in s:
            if self.stack and self.stack[-1] == char:
                self.stack.pop()
                
            else:
                self.stack.append(char)
        
        return "".join(self.stack)
        
