"""
66. Plus One
Difficulty: Easy
Link: https://leetcode.com/problems/plus-one/
Approach: Walk from the last digit; 9s become 0, first non-9 gets +1. If all 9s, prepend 1.
Time: O(n) | Space: O(1)
"""

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
