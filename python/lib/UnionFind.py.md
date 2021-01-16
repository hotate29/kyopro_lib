---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# UnionFind\n# unionfind\n\nfrom typing import Any, Optional, Callable, List\n\
    \n\nclass UnionFind:\n    def __init__(\n            self,\n            n: int,\n\
    \            v: Optional[List] = None,\n            func: Optional[Callable] =\
    \ lambda x, y: x + y\n    ) -> None:\n        self.forest = [-1] * n\n       \
    \ self.func = func\n        if v is None:\n            v = [0] * n\n        self.v\
    \ = v\n\n    def union(self, x: int, y: int) -> None:\n        x = self.findRoot(x)\n\
    \        y = self.findRoot(y)\n        if x == y:\n            return\n      \
    \  if self.forest[x] > self.forest[y]:\n            x, y = y, x\n        self.v[x]\
    \ = self.func(self.v[x], self.v[y])\n        self.forest[x] += self.forest[y]\n\
    \        self.forest[y] = x\n        return\n\n    def findRoot(self, x: int)\
    \ -> int:\n        if self.forest[x] < 0:\n            return x\n        else:\n\
    \            self.forest[x] = self.findRoot(self.forest[x])\n            return\
    \ self.forest[x]\n\n    def issame(self, x: int, y: int) -> bool:\n        return\
    \ self.findRoot(x) == self.findRoot(y)\n\n    def get_value(self, x: Any):\n \
    \       return self.v[self.findRoot(x)]\n\n    def size(self, x: int) -> int:\n\
    \        return -self.forest[self.findRoot(x)]\n"
  dependsOn: []
  isVerificationFile: false
  path: python/lib/UnionFind.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: python/lib/UnionFind.py
layout: document
redirect_from:
- /library/python/lib/UnionFind.py
- /library/python/lib/UnionFind.py.html
title: python/lib/UnionFind.py
---
