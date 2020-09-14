from binarytree import build

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        UNCOVERED, COVERED, CAMERA = range(3)
        def dfs(root, result):
            left = dfs(root.left, result) if root.left else COVERED
            right = dfs(root.right, result) if root.right else COVERED
            if left == UNCOVERED or right == UNCOVERED:
                result[0] += 1
                return CAMERA
            if left == CAMERA or right == CAMERA:
                return COVERED
            return UNCOVERED
        
        result = [0]
        if dfs(root, result) == UNCOVERED:
            result[0] += 1
        return result[0]

n=int(input())
nodes =list(map(int,input().split())) 
binary_tree = build(nodes)
val=Solution()
print(val.minCameraCover(binary_tree))
