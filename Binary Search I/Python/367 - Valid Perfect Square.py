class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        e = num
        while(s<=e):
            mid = s+(e-s)//2
            if(mid*mid==num):
                return True
            elif (mid*mid>num):
                e = mid-1
            else:
                s = mid+1
        return False