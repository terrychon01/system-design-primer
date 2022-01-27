
import collections
from queue import Queue
# from turtle import right


class newNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        


def rightSideView(root) -> list[int]:
    
    look_up = {}
    
    def dfs(node, depth):
        if not node:
            return
        look_up[depth] = node.val
        dfs(node.left, depth+1)
        dfs(node.right, depth+1)
        
    dfs(root, 0)
        
    return list(look_up.values())




if __name__ == "__main__":
    
    # root = TreeNode([1, 2, 3, None, 5, None, 4])
    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    
    out = rightSideView(root)
    
    print(out)