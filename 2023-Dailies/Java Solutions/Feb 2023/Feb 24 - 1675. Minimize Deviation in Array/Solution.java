import java.util.PriorityQueue;

public class Solution {
    public int minimumDeviation(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        int min = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num % 2 == 1) {
                num *= 2;
            }
            min = Math.min(min, num);
            pq.offer(num);
        }
        int diff = Integer.MAX_VALUE;
        while (pq.peek() % 2 == 0) {
            int max = pq.poll();
            diff = Math.min(diff, max - min);
            min = Math.min(max / 2, min);
            pq.offer(max / 2);
        }
        return Math.min(diff, pq.peek() - min);
    }
}