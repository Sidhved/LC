# Finding the Minimum Extra Charaters in a String

### 1. String Manipulation and Substring Matching

- We will need to consider all possible substring of s and check if they are present in the dictionary

### 2. Dynamic Programming Approach: (Complexity - n^2)

- We will define dp[i] as the minimum number of extra characters when considering the string s[0:i]
- **Initialization**: Create an array dp of length |s|+1, initialized with a large value. Set dp[0]=0
- **Main Algorithm**:
  - Iterate through the string from 1 to |s|
    - For each i, set dp[i] = dp[i-1] + 1 as a worst case scenario
    - Update dp[i] based on substrings of s ending at i that are in the dictionary. Use dp[i-len(substring)] for this.

### 3. Dynamic Programming with Trie: (Complexity - n*m)

The key to speeding up the solution is avoiding the creation of substrings. We achieve this by using a Trie data structure, which allows us to check if a substring exists in the dictionary without actually creating it.

- **Define a TrieNode Class**: Each node in the Trie represents a character and has a dictionary of children and a flag indicating whether it's the end of the word.
- **Building the Trie**: The trie is built from the given dictionary. Each word in the dictionary is inserted into the Trie character by character.
- **Initialize DP Array**: We use an array dp where dp[i] represents the minimum number of extra characters needed for the substring s[i:]
- **Fill DP array**:
  - Iterate through the string s from right to left
    - For each index start, initialize dp[start] = dp[start+1]+1 as the base case.
    - Traverse the Trie to find substrings that start at the index start and update dp[start] accordingly.
