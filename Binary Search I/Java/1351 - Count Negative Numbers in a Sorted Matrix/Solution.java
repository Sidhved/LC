class Solution {
    public int countNegatives(int[][] grid) {
        int n=grid.length,m=grid[0].length, row=0, column=m - 1,ans=0;
          while (row < n) {
              while (column >= 0 && grid[row][column] < 0) column--;
              ans += m - column - 1;
              row++;
          }
          return ans;
    }
}