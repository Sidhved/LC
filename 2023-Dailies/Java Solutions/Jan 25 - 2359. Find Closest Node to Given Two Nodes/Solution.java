class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int[] d1 = calcDis(edges, node1), d2 = calcDis(edges, node2);
        int ans = -1, n = edges.length;
        for (int i = 0, minDis = n; i < n; ++i) {
            var d = Math.max(d1[i], d2[i]);
            if (d < minDis) {
                minDis = d;
                ans = i;
            }
        }
        return ans;
    }

    int[] calcDis(int[] edges, int x) {
        var n = edges.length;
        var dis = new int[n];
        Arrays.fill(dis, n);
        for (var d = 0; x >= 0 && dis[x] == n; x = edges[x])
            dis[x] = d++;
        return dis;
    }
}