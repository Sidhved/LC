# Detecting cycles in a linked list

## Key concepts

1. Node Anatomy: Each node in the list contains an integer value and a next pointer that points to the subsequent node in the list
2. Cycle detection: The primary task is to identify whether a cycle exists within the list. If a cycle is detected, the function should return True, else return False
3. Memory Efficiency: The question poses an implicit challenge: To dolve it using O(1) memory, meaning constant extra space.

## Strategies

1. **Hash Table method(Complexity O(n), O(n))**: This approach involves storing visited nodes in a hash table. During traversal, if a node is encountered that already exists in the hash table, a cycle is confirmed.

- The basic idea is to traverse the list and keep a record of the nodes we've visited so far. If at any point we encounter a node that we have already visited, we can conclude that there is a cycle in the list.
- Create an empty set, visited_nodes, to keep track of the nodes that have been visited.
- Traverse the list starting from the head node.
- At each node, chec whether it already exists in visited_nodes
- If it does, return True as a cycle is detected.
- Otherwise, add the node to visited_nodes.

2.**Two-Pointers Method (Floyd's Cycle Finding Algorithm) (Complexity O(n), O(1))**: Also known as the "hare and tortoise" algorithm, this method employs two pointers that move at different speeds. If there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the cycle's existence.

- Initialize two pointers, slow_pointer and fast_pointer, both pointing to the head node initially.
- Traverse the list until the fast pointer or its next becomes None.
- Update slow_pointer = slow_pointer.next and fast_pointer = fast_pointer.next.next
- If slow_pointer and fast_pointer meet at some point, return True
