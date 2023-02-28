# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def generate_tree(x, y, length):
            value = grid[x][y]
            flag = True
            root = Node(False, False, None, None, None, None)
            for i in range(int(length)):
                for j in range(int(length)):
                    if grid[x+i][y+j] != value:
                        flag = False
                        break
            if flag:
                root.isLeaf = True
                root.val = True if value==1 else False
            else:
                root.isLeaf = False
                next_length = length // 2
                root.topLeft = generate_tree(x, y, next_length)
                root.topRight = generate_tree(x, y+next_length, next_length)
                root.bottomLeft = generate_tree(x+next_length, y, next_length)
                root.bottomRight = generate_tree(x+next_length, y+next_length, next_length)
            return root
            
        
        length = len(grid)
        # root = Node(False, False, None, None, None, None)
        return generate_tree(0, 0, length)