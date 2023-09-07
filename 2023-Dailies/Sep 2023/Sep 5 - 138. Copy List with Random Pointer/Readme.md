# Deep Copy of the linked list

- We are required to return a deep copy of the list, meaning that new list should consist of entirely new nodes that do not refer to nodes in the original list.

## Strategies

**1. Hash Map Method(Complexity:O(n), O(n)):** This approach leverages a hash map to store the mapping between each node in the original list and its corresponding node in the copied list.

- Create an empty hash map, old_to_new, to store the mapping from old nodes to new nodes.
- Traverse the original list and for each node, create a corresponding new node.
- Store the mapping in old_to_new.
- Traverse the original list again
- For each node, set its corresponding new node's next and random pointers based on the hash map.
**2. Interweaving Nodes Method (Complexity: O(n), O(1)):** This approach cleverly interweaves the nodes of the copied list with the original list, using structure to adjust the random pointers correctly, and then separate them.
- Traverse the original list.
- For each node, create a corresponding new node and place it between the current node and the current node's next node.
- Traverse the interweaved list.
- For each old node, set its correspondnig new node's random pointer.
- Traverse the interweaved list again to separate the old and new lists.
