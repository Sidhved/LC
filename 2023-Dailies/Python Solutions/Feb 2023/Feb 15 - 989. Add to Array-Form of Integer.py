from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_value = 0
                
        for val in num:            
            num_value = num_value * 10 + val
                
        sum_value = num_value + k
        
        if sum_value == 0:
            return [0]
        
        results = []
        while sum_value > 0:            
            results.insert(0, sum_value % 10)            
            sum_value = sum_value // 10
        
        return results