from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ret = 0
        s = 0
        hash_map = {}
        hash_map[0] = 1
        for n in nums:
            s += n 
            if s % k in hash_map:
                ret += hash_map[s % k]
            hash_map[s % k] = hash_map.get(s % k, 0) + 1
        return ret