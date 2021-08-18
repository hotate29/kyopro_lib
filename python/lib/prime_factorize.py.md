---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u7D20\u56E0\u6570\u5206\u89E3\n# pf\nfrom typing import List, Tuple\n\n\
    \ndef prime_factorize(n: int) -> List[Tuple[int, int]]:\n    r = []\n    for p\
    \ in range(2, n):\n        if p * p > n:\n            break\n        e = 0\n \
    \       if n % p == 0:\n            while(n % p == 0):\n                n //=\
    \ p\n                e += 1\n            r.append((p, e))\n    if n != 1:\n  \
    \      r.append((n, 1))\n    return r\n\n\nif __name__ == \"__main__\":\n    n\
    \ = int(input())\n    r = prime_factorize(n)\n    ans = []\n    for p, e in r:\n\
    \        p = str(p)\n        for i in range(e):\n            ans.append(p)\n \
    \   print(f\"{n}:\", \" \".join(ans))\n"
  dependsOn: []
  isVerificationFile: false
  path: python/lib/prime_factorize.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: python/lib/prime_factorize.py
layout: document
redirect_from:
- /library/python/lib/prime_factorize.py
- /library/python/lib/prime_factorize.py.html
title: python/lib/prime_factorize.py
---
