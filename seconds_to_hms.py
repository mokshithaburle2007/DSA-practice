"""Convert seconds to hours, minutes, seconds. Example: 7284 -> 2 hr : 1 min : 24 sec"""

n = int(input())
a = n // 3600            # hours
b = (n % 3600) // 60     # minutes
c = (n % 3600) % 60      # seconds
print(f"{a} hr : {b} min : {c} sec")
