# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind



from python.lib.UnionFind import UnionFind


n,q = map(int,input().split())
uf = UnionFind(n)
for _ in range(q):
    ti,ui,vi = map(int,input().split())
    if ti:
        print(int(uf.issame(ti,vi)))
    else:
        uf.union(ui,vi)
