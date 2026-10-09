"""
344. Reverse String
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-string/
Approach: Two pointers swapping from both ends, in place.
Time: O(n) | Space: O(1)
"""

class Solution:
    def reverseString(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
