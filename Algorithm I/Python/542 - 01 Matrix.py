"""
Standard BFS
The same idea, but use BFS to implement.
The time complexity is `O(N)`, **N is the number of element in the 2D matrix**.
The space complexity is `O(N)`, where we store the `opt`.
"""
import collections


class Solution(object):
    def updateMatrix(self, matrix):
        M, N = len(matrix), len(matrix[0])
        opt = [[-1]*N for _ in range(M)]
        q = collections.deque([])

        for i in range(M):
            for j in range(N):
                if matrix[i][j]==0:
                    q.append((i, j, 0))

        while q:
            i, j, dis = q.popleft()
            if i<0 or i>=M: continue
            if j<0 or j>=N: continue
            if opt[i][j]!=-1: continue
            opt[i][j] = dis

            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                q.append((ni, nj, dis+1))

        return opt