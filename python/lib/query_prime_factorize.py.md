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
  code: "# \uFF08\u30AF\u30A8\u30EA\uFF09\u7D20\u56E0\u6570\u5206\u89E3\n# query_pf\n\
    from typing import List, Tuple\n\n\nclass prime_factorize():\n    def __init__(self,\
    \ max_n) -> None:\n        self.max_n = max_n\n        self.minfactor = [i for\
    \ i in range(max_n + 1)]\n        for i in range(2, max_n):\n            if i\
    \ * i > max_n:\n                break\n            else:\n                if i\
    \ == self.minfactor[i]:\n                    for j in range(i, max_n + 1, i):\n\
    \                        if self.minfactor[j] == j:\n                        \
    \    self.minfactor[j] = i\n\n    def pf(self, n: int) -> List[Tuple[int, int]]:\n\
    \        assert 0 < n <= self.max_n\n        r = []\n        while(n != 1):\n\
    \            e = 0\n            p = self.minfactor[n]\n            while(n % p\
    \ == 0):\n                e += 1\n                n //= p\n            r.append((p,\
    \ e))\n        return r\n\n\nif __name__ == \"__main__\":\n    pf = prime_factorize(10**7)\n\
    \    while(True):\n        i = int(input())\n        print(i, pf.pf(i))\n"
  dependsOn: []
  isVerificationFile: false
  path: python/lib/query_prime_factorize.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: python/lib/query_prime_factorize.py
layout: document
redirect_from:
- /library/python/lib/query_prime_factorize.py
- /library/python/lib/query_prime_factorize.py.html
title: python/lib/query_prime_factorize.py
---
