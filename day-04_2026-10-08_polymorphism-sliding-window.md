# Day 04 - 08/10/2026 - Polymorphism, Sliding Window

## Polymorphism
Polymorphism means one thing exists in many forms.
1. Method overloading
2. Method overriding

- In Python, method overloading is **not achieved by default**. Defining the same method twice just replaces the first.
- Workaround: **variable-length arguments** (`*args`), where the number of arguments is not fixed (dynamic).

## When there is a repetition condition
Think of: **dictionaries / hash map, stack**.

## Sliding Window (intro)
Given `k` = window size, e.g. array `[2, 8, 7, 12, 15]`.
- **Static window size**: `k` does not change.

### How to identify that a problem is a sliding window problem
1. The problem **gives a `k` value**.
2. It mentions **consecutive / sub-array / sub-string** for a `k` value.

## LeetCode (sliding window)
- 643. Maximum Average Subarray I
- 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
