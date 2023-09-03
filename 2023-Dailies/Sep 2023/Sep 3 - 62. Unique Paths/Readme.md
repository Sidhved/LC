# Unique Paths

## Points to Consider

- Grid Dimensions: The grid dimensions are m rows and n columns, with 1 <= m, n, <= 100
- Movement constraints: The robot can only move either  down or to the right at any given point. It cannot move diagonally or backwards.
- Dynamic Programming and Combinatorial Mathematics: The problem can be solved using either Dynamic Programming Approach or using Combinatorial Mathematics.

### Dynamic Programming Approach (Complexity = O(m\*n)

- The idea behind this approach is to use a 2D DP array to store the number of unique paths to each cell. A cell (i, j) can be reached either from (i-1,j) or (i, j-1). Thus, the number of unique paths to (i, j) is the sum of the number of unique paths to these two cells.
  - Initialization: Create a m\*n DP array, initializing the first row and first column to 1 because there is only one way to reach those cells from the starting point.
  - Iterate over the DP array starting from cell (1,1).
  - For each cell(i, j), set \text{dp}[i][j]= \text{dp}[i-1][j] + \text{dp}[i][j-1]

### Memory Optimized Dynamic Programming

- The original DP solution used a m\*n array to store the number of unique paths to each cell. However, since we only need information from the previous row and the current row to compute the number of unique paths for a given cell, we can optimize the solution to use only two rows at a time. This reduces the space complexity O(m\*n) to O(n).
- In the original O(m\*n) approach, we used a 2D array dp where  \text{dp}[i][j] represented the number of unique paths to reach cell (i, j). To optimize this to O(n), we can maintain only two 1D arrays: prev_row and curr_row, each of length n.
  - prev_row[j] will represent \text{dp}[i-1][j], the number of unique paths to reach the cell in the previous row and jth column
  - curr_row[j] will represent \text{dp}[i][j], the number of unique paths to reach the cell in the current row and jth column
- Initialization: Initialize two 1D arrays curr_row and prev_row with n elements, setting all elements to 1.
- Iterate over the rows starting from 1 (the second row)
- For each cell (i, j), set curr_row[j] = curr_row[j-1]+prev_row[j]
- Swap curr_row and prev_row for the next iteration.

### Combinatorial Mathematics - Complexity: O(m) or O(n)

- The number of unique paths can be seen as the number of ways to choose m-1 downs and n-1 rights, regardless of the order. In combinatorial terms, this is equivalent to \binom{m+n-2}{m-1}
- Use the combinatorial formula: \binom{m+n-2}{m-1} or \binom{m+n-2}{n-1} to calculate the number of unique paths.
- Python's Math Library:Python provides a built-in function math.comb(n, k), to calculate \binom{n}{k} efficiently.
