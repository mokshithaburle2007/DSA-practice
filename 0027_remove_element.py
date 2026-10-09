"""
27. Remove Element
Difficulty: Easy
Link: https://leetcode.com/problems/remove-element/
Approach: Write pointer k copies every element that is not val.
Time: O(n) | Space: O(1)
"""

class Solution:
    def removeElement(self, nums, val):
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k
