# Day 01 - 05/10/2026 - Python Basics

## Python
- Python is an **interpreted** language: it executes **line by line**.
- The default input in Python is a **string**, so convert with `int(input())`.

## Data types
- Basic: `int`, `float`, `bool`, `str`
- Sequence / collection types: `list`, `dict`, `tuple`, `set`, `range`

## Operators
- **Arithmetic**: `+  -  *  %  /  //  **`
  - `^` is **XOR** in Python, not power. Use `**` for power.
  - `5 % 13 = 5` (if the left operand is smaller than the right, the answer is the left operand)
- **Logical**: `and`, `or`, `not`
- **Relational**: `<  >  <=  >=  ==  !=`
- **Assignment**: `=  +=  -=  ...`
- **Bitwise**: AND `&`, OR `|`, left shift `<<`, right shift `>>`

```
5 & 4            5 | 4
101              101
100              100
---              ---
100 = 4          101 = 5
```
- Right shift: `n >> k` = `n / 2^k` (floor)
- **Membership**: `in`, `not in`

## Conditional statements
- simple `if`
- `if` / `else`
- `if` / `elif` / `else`

## Control statements
- `break`: forcefully stops execution of the loop
- `continue`: skips the rest of this iteration and continues the loop

## Loops
- `for` loop and `while` loop are **entry-checking** loops.
- **Important:** Python does **not** support `do-while` (exit-checking).

```python
for i in range(start, end, skip):
    ...
```

Even numbers program:
```python
for i in range(0, 101, 2):
    print(i)             # line by line
    print(i, end=" ")    # single line
```

## Formatted string
```python
print(f"{i} - even number = {i}")   # i is the iteration variable
```

## Programs from this day
- [`python-basics/prime_numbers.py`](../python-basics/prime_numbers.py)
- [`python-basics/seconds_to_hms.py`](../python-basics/seconds_to_hms.py)
