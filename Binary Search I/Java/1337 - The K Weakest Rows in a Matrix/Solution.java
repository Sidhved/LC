import java.util.Arrays;

class Solution {
    public static int numOnes(int[] row) {
        int lo = 0;
        int hi = row.length;
        
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            
            if (row[mid] == 1)
                lo = mid + 1;
            else
                hi = mid;
        }
        
        return lo;
    }
    public int[] kWeakestRows(int[][] mat, int k) {
        int rows = mat.length;
    int cols = mat[0].length;

    int[] score = new int[rows];
    int j;
    for (int i = 0; i < rows; i++) {
         j = numOnes(mat[i]);
        score[i] = j * rows + i;
    }

    Arrays.sort(score);
    for (int i = 0; i < k; i++) {
        score[i] = score[i] % rows;
    }

    return Arrays.copyOfRange(score, 0, k);
    }
}