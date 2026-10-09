# Day 05 - 09/10/2026 - Sliding Window Steps, Inheritance

## Sliding window (fixed size) - steps
1. Start with `i = 0`, `j = 0`.
2. **Window size not achieved**, i.e. `j - i + 1 < k`: do `j += 1`.
3. **Window size achieved**, i.e. `j - i + 1 == k`: compute the answer, then slide with `i += 1` and `j += 1`.

Template: [`templates/sliding_window_fixed.py`](../templates/sliding_window_fixed.py)

## Inheritance
The child class gets features from the parent class.

Types:
- Single
- Multiple
- Multilevel
- Hierarchical
- Hybrid

Examples: [`python-basics/inheritance.py`](../python-basics/inheritance.py)
