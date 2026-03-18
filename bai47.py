class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        c = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue or ruleKey == "color" and item[1] == ruleValue or ruleKey == "name" and item[2] == ruleValue:
                c+=1        
        return c