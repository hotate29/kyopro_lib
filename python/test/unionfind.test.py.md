---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \n\nfrom python.lib.UnionFind import UnionFind\n\n\nn, q = map(int, input().split())\n\
    uf = UnionFind(n)\nfor _ in range(q):\n    ti, ui, vi = map(int, input().split())\n\
    \    if ti:\n        print(int(uf.issame(ui, vi)))\n    else:\n        uf.union(ui,\
    \ vi)\n"
  dependsOn: []
  isVerificationFile: true
  path: python/test/unionfind.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: python/test/unionfind.test.py
layout: document
redirect_from:
- /verify/python/test/unionfind.test.py
- /verify/python/test/unionfind.test.py.html
title: python/test/unionfind.test.py
---
