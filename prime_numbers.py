"""Prime number programs (3 levels), from Day 01 notes."""


# Level I: count the divisors. A prime has exactly 2 (1 and itself).
def is_prime_count(a):
    c = 0
    for i in range(1, a + 1):
        if a % i == 0:
            c += 1
    return c == 2


# Level II: try every i from 2 to n-1; any divisor means not prime.
def is_prime_basic(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Level III: only need to check up to n/2 (use integer division).
def is_prime_half(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


# Level IV: only need to check up to sqrt(n). Best of the three: O(sqrt n).
def is_prime_sqrt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    print("prime" if is_prime_sqrt(n) else "not prime")
