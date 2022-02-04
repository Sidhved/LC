class Solution {
    private void helper(int[][] distance, int left, int right, int K) {
        if (left >= right) {
            return;
        }

        int pos = partition(distance, left, right);
        if (pos == K) {
            return;
        } else if (pos < K) {
            helper(distance, pos + 1, right, K);
        } else {
            helper(distance, left, pos - 1, K);
        }
    }
    public int[][] kClosest(int[][] points, int K) {
        int[][] distances = new int[points.length][2];
        for (int i = 0; i < points.length; i++) {
            distances[i][0] = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            distances[i][1] = i;
        }

        helper(distances, 0, distances.length - 1, K - 1);
        int[][] rst = new int[K][2];
        for (int i = 0; i < K; i++) {
            rst[i][0] = points[distances[i][1]][0];
            rst[i][1] = points[distances[i][1]][1];
        }
        return rst;
    }
    
    private int partition(int[][] distance, int left, int right) {
        int less = left - 1, more = right;
        while (left < more) {
            if (distance[left][0] < distance[right][0]) {
                swap(distance, ++less, left++);
            } else if (distance[left][0] > distance[right][0]) {
                swap(distance, left, --more);
            } else {
                left++;
            }
        }
        swap(distance, more, right);
        return less + 1;
    }
    private void swap(int[][] distance, int a, int b) {
        int t1 = distance[a][0], t2 = distance[a][1];
        distance[a][0] = distance[b][0];
        distance[a][1] = distance[b][1];
        distance[b][0] = t1;
        distance[b][1] = t2;
    }
}