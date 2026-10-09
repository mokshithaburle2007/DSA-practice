"""Common ways to loop over a list."""

n = [4, 8, 15, 16, 23, 42]

# sum of all elements
total = 0
for i in range(0, len(n)):
    total += n[i]
print("sum:", total)

# alternate elements
for i in range(0, len(n), 2):
    print(n[i], end=" ")
print()

# list in reverse
for i in range(len(n) - 1, -1, -1):
    print(n[i], end=" ")
print()
