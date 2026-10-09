"""
9. Palindrome Number
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/
Approach: Reverse the number mathematically and compare. Negatives are never palindromes.
Time: O(log n) | Space: O(1)
"""

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        original, rev = x, 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        return original == rev
