class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def find(nums, k):
          ans, M = 0, len(nums)
          
          ''' Choose two numbers. '''
          for i in range(M):
            for j in range(i+1, M):
              t = nums[:i] + nums[i+1:j] + nums[j+1:]
              ans = max(ans, k*gcd(nums[i], nums[j]) + find(t, k+1))
          return ans
          
        return find(tuple(nums), 1)