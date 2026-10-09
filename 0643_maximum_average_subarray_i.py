"""
643. Maximum Average Subarray I
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-average-subarray-i/
Approach: Fixed-size sliding window of size k, tracking the max window sum.
Time: O(n) | Space: O(1)
"""

class Solution:
    def findMaxAverage(self, nums, k):
        i = j = 0
        window_sum = 0
        best = float("-inf")
        while j < len(nums):
            window_sum += nums[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                best = max(best, window_sum)
                window_sum -= nums[i]
                i += 1
                j += 1
        return best / k
