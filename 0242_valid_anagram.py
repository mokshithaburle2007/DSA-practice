"""
242. Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/
Approach: Count characters of s in a dict, subtract for t; all counts must be zero.
Time: O(n) | Space: O(1) (26 letters)
"""

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in t:
            if freq.get(ch, 0) == 0:
                return False
            freq[ch] -= 1
        return True
