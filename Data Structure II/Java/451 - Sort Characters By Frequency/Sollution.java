class Solution {
    public String frequencySort(String s) {
        if (s == null || s.length() == 0) {
         return s;
      }

      HashMap<Character, Integer> hm = new HashMap();
      StringBuilder sb = new StringBuilder();
      PriorityQueue<Character> heap = new PriorityQueue<Character>((a, b) -> hm.get(b) - hm.get(a));

      for (Character c : s.toCharArray()) {
         hm.put(c, hm.getOrDefault(c, 0) + 1);
      }

      for (Map.Entry<Character, Integer> en : hm.entrySet()) {
         heap.offer(en.getKey());
      }

      while (!heap.isEmpty()) {
         Character c = heap.poll();
         int count = hm.get(c);

         while (count != 0) {
            sb.append(c);
            count--;
         }
      }

      return sb.toString();    
    }
}