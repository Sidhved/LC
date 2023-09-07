# Splitting the linked list into K consecutive Paths

(Complexity O(n), O(k))

- The core idea is to first calculate the length of the lniked list to determine the base size of each part and the number of parts that should have an extra node. Then, we traverse the list to construct each part based on these calculations.
- Initialize the var length to store the length of the list.
- Initialize the empty list parts to store the resulting parts.
- Traverse the linked list to find its length
- Calculate base_size and extra using divmod(length, k)
- Traverse the linked list again
- For each part, construct a sublist with base_size nodes.
- If extra > 0, add one more node to the current part and decrement extra.
- Append each constructed part to the parts list.
