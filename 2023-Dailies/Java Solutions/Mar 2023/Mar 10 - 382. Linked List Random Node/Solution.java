/**
 * Definition for singly-linked list.*/
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Solution {
    private HashMap<Integer, Integer> indexToNum;
    private int size = 0;
    private Random r;
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        indexToNum = new HashMap<Integer, Integer>();
        while (head != null) {
            indexToNum.put(size++, head.val);
            head = head.next;
        }
        r = new Random();
    }

    /** Returns a random node's value. */
    public int getRandom() {
        if (size > 0) {
            int index = r.nextInt(size);
            int val = indexToNum.get(index);
            return val;
        }
        return -1;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */