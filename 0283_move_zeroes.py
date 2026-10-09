"""
283. Move Zeroes
Difficulty: Easy
Link: https://leetcode.com/problems/move-zeroes/
Approach: Write pointer collects non-zeros in order, then fill the rest with zeros.
Time: O(n) | Space: O(1)
"""

class Solution:
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
