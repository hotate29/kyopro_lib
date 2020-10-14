from typing import List, Tuple


class prime_factorize():
    def __init__(self, max_n) -> None:
        self.max_n = max_n
        self.minfactor = [i for i in range(max_n + 1)]
        for i in range(2, max_n):
            if i * i > max_n:
                break
            else:
                if i == self.minfactor[i]:
                    for j in range(i, max_n + 1, i):
                        self.minfactor[j] = i

    def pf(self, n: int) -> List[Tuple[int, int]]:
        assert n <= self.max_n
        r = []
        while(n != 1):
            e = 0
            p = self.minfactor[n]
            while(n % p == 0):
                e += 1
                n //= p
            r.append((p, e))
        return r


if __name__ == "__main__":
    pf = prime_factorize(10**5)
    for i in range(1,10**5):
        r = pf.pf(i)
        print(r)