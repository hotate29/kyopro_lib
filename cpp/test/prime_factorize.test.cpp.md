---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cpp/lib/prime_factorize.hpp
    title: cpp/lib/prime_factorize.hpp
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    '*NOT_SPECIAL_COMMENTS*': ''
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
  bundledCode: "#line 1 \"cpp/test/prime_factorize.test.cpp\"\n#define PROBLEM \"\
    http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A\"\n\n#include\
    \ <iostream>\n#line 1 \"cpp/lib/prime_factorize.hpp\"\n#include <vector>\n\nusing\
    \ namespace std;\n\nvector<pair<long long, long long>> prime_factorize(long long\
    \ n)\n{\n    vector<pair<long long, long long>> ret;\n    long long e = 0;\n \
    \   for (long long i = 2; i < n; ++i)\n    {\n        if (i * i > n)\n       \
    \     break;\n        if (n % i == 0)\n        {\n            while (n % i ==\
    \ 0)\n            {\n                n /= i;\n                ++e;\n         \
    \   }\n        }\n        ret.emplace_back(make_pair(i, e));\n        e = 0;\n\
    \    }\n    if (n!=1) ret.emplace_back(make_pair(n,1));\n    return ret;\n}\n\
    #line 5 \"cpp/test/prime_factorize.test.cpp\"\nusing namespace std;\n\n\nint main(){\n\
    \    int n; cin >> n;\n    auto r = prime_factorize(n);\n    cout << n << \":\"\
    ;\n    for (auto pe:r){\n        for (int i=0; i<pe.second;++i){\n           \
    \ cout << \" \" << pe.first;\n        }\n    }\n    cout << endl;\n}\n"
  code: "#define PROBLEM \"http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A\"\
    \n\n#include <iostream>\n#include \"../lib/prime_factorize.hpp\"\nusing namespace\
    \ std;\n\n\nint main(){\n    int n; cin >> n;\n    auto r = prime_factorize(n);\n\
    \    cout << n << \":\";\n    for (auto pe:r){\n        for (int i=0; i<pe.second;++i){\n\
    \            cout << \" \" << pe.first;\n        }\n    }\n    cout << endl;\n\
    }"
  dependsOn:
  - cpp/lib/prime_factorize.hpp
  isVerificationFile: true
  path: cpp/test/prime_factorize.test.cpp
  requiredBy: []
  timestamp: '2020-10-18 00:08:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: cpp/test/prime_factorize.test.cpp
layout: document
redirect_from:
- /verify/cpp/test/prime_factorize.test.cpp
- /verify/cpp/test/prime_factorize.test.cpp.html
title: cpp/test/prime_factorize.test.cpp
---
