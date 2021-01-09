# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        sumLeft = 0
        openList = deque()
        closedList = deque()
        openList.append(root)
        closedList.append(root)
        while openList:
            curr = openList[-1]
            closedList.append(curr.val)
            openList.pop()
            if curr.right is not None:
                openList.append(curr.right)
            if curr.left is not None:
                openList.append(curr.left)
                if curr.left.left is None and curr.left.right is None:
                    sumLeft = sumLeft + curr.left.val
        return sumLeft