---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A\n\
    \n\nfrom python.lib.prime_factorize import prime_factorize as pf\n\n\nif __name__\
    \ == \"__main__\":\n    n = int(input())\n    r = pf(n)\n    ans = []\n    for\
    \ p, e in r:\n        p = str(p)\n        for i in range(e):\n            ans.append(p)\n\
    \    print(f\"{n}:\", \" \".join(ans))\n"
  dependsOn: []
  isVerificationFile: true
  path: python/test/prime_factorize.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: python/test/prime_factorize.test.py
layout: document
redirect_from:
- /verify/python/test/prime_factorize.test.py
- /verify/python/test/prime_factorize.test.py.html
title: python/test/prime_factorize.test.py
---
