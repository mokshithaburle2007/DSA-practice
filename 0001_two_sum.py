"""
1. Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
Approach: One pass with a hash map of value -> index; look up the complement.
Time: O(n) | Space: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
