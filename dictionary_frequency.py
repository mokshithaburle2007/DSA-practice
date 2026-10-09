"""Dictionary basics and frequency counting."""

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(d.keys())
print(d.values())
print(d.items())

arr = [1, 2, 3, 4, 2, 3]
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
print(freq)   # {1: 1, 2: 2, 3: 2, 4: 1}
