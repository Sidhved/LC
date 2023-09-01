# How to merge and sort an array?

## 1.Naive Approach(STL) - Complexity: O((m+n)log(m+n))

- Append or merge the sencond array at the end of the first array and sort the entire array.

## 2. Two Pointer - Complexity: O(m+n)

- We start with two pointers i and j, initialized to m-1 and n-1 respectively. We also have another pointer k initialized to m+n-1, which will be used to keep track of the position in nums1 where we will be placing the larger element. Then we can start iterating from the end of the arrays i and j, and compare  the elements at these positions. We will place the alrger element in nums1 at position k and decrement the corresponding pointer i and j accordingly. We will continue doing this usitl we have iterated through all the elements in nums2. If there are still elements left in nums1, we dont need to do anything as they are already sorted and in correct place.
