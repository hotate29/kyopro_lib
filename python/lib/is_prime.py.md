---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: python/test/is_prime.test.py
    title: python/test/is_prime.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u7D20\u6570\u5224\u5B9A\n# isprime\ndef isprime(n: int) -> bool:\n   \
    \ if n < 2 or n % 2 == 0 and not n == 2:\n        return False\n    for i in range(3,\
    \ n + 1, 2):\n        if i * i <= n:\n            if n % i == 0:\n           \
    \     return False\n        else:\n            break\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: python/lib/is_prime.py
  requiredBy: []
  timestamp: '2020-11-06 23:29:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - python/test/is_prime.test.py
documentation_of: python/lib/is_prime.py
layout: document
redirect_from:
- /library/python/lib/is_prime.py
- /library/python/lib/is_prime.py.html
title: python/lib/is_prime.py
---
