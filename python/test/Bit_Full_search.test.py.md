---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: python/lib/Bit_Full_search.py
    title: python/lib/Bit_Full_search.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A\n\
    from python.lib.Bit_Full_search import BitFullSearch\n\n\nn = int(input())\na\
    \ = list(map(int,input().split()))\nq = int(input())\nm = list(map(int,input().split()))\n\
    \nc = {sum(ci) for ci in BitFullSearch(a)}\nfor mi in m:\n    if mi in c:\n  \
    \      print(\"yes\")\n    else:\n        print(\"no\")\n"
  dependsOn:
  - python/lib/Bit_Full_search.py
  isVerificationFile: true
  path: python/test/Bit_Full_search.test.py
  requiredBy: []
  timestamp: '2020-11-07 21:56:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: python/test/Bit_Full_search.test.py
layout: document
redirect_from:
- /verify/python/test/Bit_Full_search.test.py
- /verify/python/test/Bit_Full_search.test.py.html
title: python/test/Bit_Full_search.test.py
---
