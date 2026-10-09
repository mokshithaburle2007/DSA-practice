"""
75. Sort Colors
Difficulty: Medium
Link: https://leetcode.com/problems/sort-colors/
Approach: Dutch national flag: low/mid/high pointers in a single pass.
Time: O(n) | Space: O(1)
"""

class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
