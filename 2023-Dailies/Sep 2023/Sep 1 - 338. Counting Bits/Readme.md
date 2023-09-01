# **How to count the number of 1's in binary of any number?**

## **1. Dynamic programming with Bit Manipulation**

- Bit manipulation allows is to count the number of 1's in an efficient manner, especially when combined with dynamic programming
- In this approach, we exploit the fact that shifting a number to the right by one bit (i.e. dividing by 2) removes the last bit. So, the number of 1's in the binary representation is the same as (x/2) + last bit of x.
- We use bitwise shift and AND operations. Bitwise right shifting x >> 1 essentially removes the last bit, and x & 1 extracts the last bit. This helps us compute the result for x using previously computed results.

## **2. Dynamic Programming with offset**

- This method uses a fascinating property of binary numbers, where number x and i+2^k share the same number of 1's, except for an additional 1 at the k-th bit for i+2^k
- This method introduces the concept of an "offset", which is a power of 2 We use this offset to calculate the number of 1's for new numbers based on previously calculated results.

|--------------------------------------------------------------------------------------------------|
