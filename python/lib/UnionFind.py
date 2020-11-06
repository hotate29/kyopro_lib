# UnionFind
# unionfind
class UnionFind:
    def __init__(self, n: int) -> None:
        self.forest = [-1] * n

    def union(self, x: int, y: int) -> None:
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        if self.forest[x] > self.forest[y]:
            x, y = y, x
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

    def size(self, x: int) -> int:
        return -self.forest[self.findRoot(x)]
