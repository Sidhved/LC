class Solution {
    public String reverseWords(String s) {
        if (s == null || s.length() < 2) {
            return s;
        }
 
        int start = 0;
        int end = 0;
 
        char[] arr = s.toCharArray();
 
        while (end < s.length()) {
            while (end < s.length() && s.charAt(end) != ' ') {
                end++;
            }
            reverse(arr, start, end - 1);
            end++;
            start = end;
        }
 
        reverse(arr, start, end - 1);
 
        return new String(arr);
    }
 
    private void reverse(char[] arr, int start, int end) {
        while (start < end) {
            char temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}