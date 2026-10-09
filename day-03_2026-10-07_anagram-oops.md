# Day 03 - 07/10/2026 - Valid Anagram, OOP Concepts

## LeetCode planned
- 347 Top K Frequent Elements
- 217 Contains Duplicate

## 242. Valid Anagram
- `LEETCODE` and `TEELDEOC` -> **anagram** (same letters, same counts)
- `ABCD` and `EFGH` -> **not an anagram**
- Solved with a frequency count (see [`leetcode/hashing/0242_valid_anagram.py`](../leetcode/hashing/0242_valid_anagram.py))

## OOP concepts
1. Encapsulation
2. Abstraction
3. Polymorphism
4. Inheritance

## `self`
`self` refers to the current object (the instance the method is called on).

```python
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name =", self.name)
```
Full example: [`python-basics/student_class.py`](../python-basics/student_class.py)
