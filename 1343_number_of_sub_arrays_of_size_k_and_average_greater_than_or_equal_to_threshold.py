"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
Approach: Fixed-size sliding window; count windows whose sum >= k * threshold.
Time: O(n) | Space: O(1)
"""

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        i = j = 0
        window_sum = 0
        count = 0
        target = k * threshold
        while j < len(arr):
            window_sum += arr[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if window_sum >= target:
                    count += 1
                window_sum -= arr[i]
                i += 1
                j += 1
        return count
