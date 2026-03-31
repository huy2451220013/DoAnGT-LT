class Solution(object):
    def isValid(self, s):
        pair = {")":"(", "]":"[", "}":"{"}
        stack = []
        for symbol in s:
            if symbol in pair.values():
                stack.append(symbol)
            elif not stack or stack.pop() != pair[symbol]:
                    return False

        return not stack