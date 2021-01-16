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
  code: "# \u7D04\u6570\u5217\u6319\n# divisors\nfrom typing import List\nfrom itertools\
    \ import chain\n\n\ndef enum_divisors(n: int) -> chain:\n    upper = []\n    lower\
    \ = []\n    i = 1\n    while i * i <= n:\n        if n % i == 0:\n           \
    \ lower.append(i)\n            if i != n // i:\n                upper.append(n\
    \ // i)\n        i += 1\n    return chain(lower,upper[::-1])"
  dependsOn: []
  isVerificationFile: false
  path: python/lib/enum_divisors.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: python/lib/enum_divisors.py
layout: document
redirect_from:
- /library/python/lib/enum_divisors.py
- /library/python/lib/enum_divisors.py.html
title: python/lib/enum_divisors.py
---
