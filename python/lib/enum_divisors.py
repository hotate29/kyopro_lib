# 約数列挙
# divisors
from typing import List
from itertools import chain


def enum_divisors(n: int) -> chain:
    upper = []
    lower = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
        i += 1
    return chain(lower,upper[::-1])