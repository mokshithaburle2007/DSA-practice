# Day 02 - 06/10/2026 - Leap Year, Lists, Dictionaries

## Leap year
A year is a leap year if it is divisible by 4 **and not by 100**, **or** divisible by 400.

```python
n = int(input())
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print("leap year")
else:
    print("not a leap year")
```
> Note: in class the condition was written as `(n%4==0 or n%400==0) and (n%100!=0)`.
> That wrongly rejects 2000 (divisible by 400 and by 100). The version above is correct.

## Looping over a list
- Sum of all elements: `for i in range(0, len(n)): sum += n[i]`
- Alternate elements: `range(0, len(n), 2)`
- Reverse order: `range(len(n)-1, -1, -1)`

## Dictionaries
```python
d = {'a': 1, 'b': 2, 'c': 3}
d.keys()     # ['a', 'b', 'c']
d.values()   # [1, 2, 3]
d.items()    # [('a', 1), ('b', 2), ('c', 3)]
```
`d.items` needs the brackets: `d.items()`.

## Frequency using a dictionary
```python
arr = [1, 2, 3, 4, 2, 3]
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
# {1: 1, 2: 2, 3: 2, 4: 1}
```

## Programs from this day
- [`python-basics/leap_year.py`](../python-basics/leap_year.py)
- [`python-basics/list_loops.py`](../python-basics/list_loops.py)
- [`python-basics/dictionary_frequency.py`](../python-basics/dictionary_frequency.py)
