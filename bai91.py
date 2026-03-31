class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                item = stack.pop()
                res[item] = i - item
            stack.append(i)
        
        return res








                       