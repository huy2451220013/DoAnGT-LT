class Solution(object):
    def levelOrder(self, root):
        res = []
        queue = [root]
        if root == None:
            return res
        while queue:
            level = []
            for i in range (len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
        