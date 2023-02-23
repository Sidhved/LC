import Queue

class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        pq1 = Queue.PriorityQueue()
        pq2 = Queue.PriorityQueue()
        for i in range(len(Profits)):
            pq1.put((Capital[i], Profits[i]))
        
        for _ in range(k):
            while not pq1.empty() and pq1.queue[0][0] <= W:
                tmp = pq1.get()
                pq2.put((-tmp[1], tmp[1]))
            if not pq2.empty():
                W += pq2.get()[1]
        return W