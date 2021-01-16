# UnionFind
# unionfind

from typing import Any, Optional, Callable, List


class UnionFind:
    def __init__(
            self,
            n: int,
            v: Optional[List] = None,
            func: Optional[Callable] = lambda x, y: x + y
    ) -> None:
        self.forest = [-1] * n
        self.func = func
        if v is None:
            v = [0] * n
        self.v = v

    def union(self, x: int, y: int) -> None:
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        if self.forest[x] > self.forest[y]:
            x, y = y, x
        self.v[x] = self.func(self.v[x], self.v[y])
        self.forest[x] += self.forest[y]
        self.forest[y] = x
        return

    def findRoot(self, x: int) -> int:
        if self.forest[x] < 0:
            return x
        else:
            self.forest[x] = self.findRoot(self.forest[x])
            return self.forest[x]

    def issame(self, x: int, y: int) -> bool:
        return self.findRoot(x) == self.findRoot(y)

    def get_value(self, x: Any):
        return self.v[self.findRoot(x)]

    def size(self, x: int) -> int:
        return -self.forest[self.findRoot(x)]
