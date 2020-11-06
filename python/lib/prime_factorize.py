# 素因数分解
# pf
from typing import List, Tuple


def prime_factorize(n: int) -> List[Tuple[int, int]]:
    r = []
    for p in range(2, n):
        if p * p > n:
            break
        e = 0
        if n % p == 0:
            while(n % p == 0):
                n //= p
                e += 1
            r.append((p, e))
    if n != 1:
        r.append((n, 1))
    return r


if __name__ == "__main__":
    n = int(input())
    r = prime_factorize(n)
    ans = []
    for p, e in r:
        p = str(p)
        for i in range(e):
            ans.append(p)
    print(f"{n}:", " ".join(ans))
