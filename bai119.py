class Solution(object):
    def preorderTraversal(self, root):
        bag = [root]
        sol = []
        while bag:
            node = bag.pop()
            if node:
                sol.append(node.val)
                bag.append(node.right)
                bag.append(node.left)
        return sol