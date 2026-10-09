"""
69. Sqrt(x)
Difficulty: Easy
Link: https://leetcode.com/problems/sqrtx/
Approach: Binary search on the answer in [0, x]; keep the largest mid with mid*mid <= x.
Time: O(log x) | Space: O(1)
"""

class Solution:
    def mySqrt(self, x):
        lo, hi, ans = 0, x, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
