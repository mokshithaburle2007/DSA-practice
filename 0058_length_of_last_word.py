"""
58. Length of Last Word
Difficulty: Easy
Link: https://leetcode.com/problems/length-of-last-word/
Approach: Scan from the end, skip trailing spaces, then count letters.
Time: O(n) | Space: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        count = 0
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        return count
