---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: python/lib/is_prime.py
    title: python/lib/is_prime.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C



    from python.lib.is_prime import isprime



    print(sum(isprime(int(input())) for _ in range(int(input()))))

    '
  dependsOn:
  - python/lib/is_prime.py
  isVerificationFile: true
  path: python/test/is_prime.test.py
  requiredBy: []
  timestamp: '2020-11-06 23:29:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: python/test/is_prime.test.py
layout: document
redirect_from:
- /verify/python/test/is_prime.test.py
- /verify/python/test/is_prime.test.py.html
title: python/test/is_prime.test.py
---
