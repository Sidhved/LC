import collections
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        queue = collections.deque([0])
        visited = set([0])
        pos = collections.defaultdict(set)
        for i, num in enumerate(arr):
            pos[num].add(i)
        level = 0
        while len(queue)>0:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == n-1: return level
                # examine the next nodes
                nexts = [node-1, node+1] + list(pos[arr[node]])
                for i in nexts:
                    if 0<=i<n and i not in visited:
                        queue.append(i)
                        visited.add(i)
                # No need to examine nodes of the same value
                pos[arr[node]] = set()
            level += 1
        return -1