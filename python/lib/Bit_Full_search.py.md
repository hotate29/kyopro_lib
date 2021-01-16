---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: python/test/Bit_Full_search.test.py
    title: python/test/Bit_Full_search.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# bit\u5168\u63A2\u7D22\n# bitfullsearch\nfrom itertools import product\n\
    \n\ndef BitFullSearch(a):\n    p = product((0,1),repeat=len(a))\n    return ([ai\
    \ for ai,bi in zip(a,pi) if bi] for pi in p)\n"
  dependsOn: []
  isVerificationFile: false
  path: python/lib/Bit_Full_search.py
  requiredBy: []
  timestamp: '2020-11-07 21:56:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - python/test/Bit_Full_search.test.py
documentation_of: python/lib/Bit_Full_search.py
layout: document
redirect_from:
- /library/python/lib/Bit_Full_search.py
- /library/python/lib/Bit_Full_search.py.html
title: python/lib/Bit_Full_search.py
---
