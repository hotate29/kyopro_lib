---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: cpp/test/prime_factorize.test.cpp
    title: cpp/test/prime_factorize.test.cpp
  _isVerificationFailed: false
  _pathExtension: hpp
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "#line 1 \"cpp/lib/prime_factorize.hpp\"\n#include <vector>\n\nusing\
    \ namespace std;\n\nvector<pair<long long, long long>> prime_factorize(long long\
    \ n)\n{\n    vector<pair<long long, long long>> ret;\n    long long e = 0;\n \
    \   for (long long i = 2; i < n; ++i)\n    {\n        if (i * i > n)\n       \
    \     break;\n        if (n % i == 0)\n        {\n            while (n % i ==\
    \ 0)\n            {\n                n /= i;\n                ++e;\n         \
    \   }\n        }\n        ret.emplace_back(make_pair(i, e));\n        e = 0;\n\
    \    }\n    if (n!=1) ret.emplace_back(make_pair(n,1));\n    return ret;\n}\n"
  code: "#include <vector>\n\nusing namespace std;\n\nvector<pair<long long, long\
    \ long>> prime_factorize(long long n)\n{\n    vector<pair<long long, long long>>\
    \ ret;\n    long long e = 0;\n    for (long long i = 2; i < n; ++i)\n    {\n \
    \       if (i * i > n)\n            break;\n        if (n % i == 0)\n        {\n\
    \            while (n % i == 0)\n            {\n                n /= i;\n    \
    \            ++e;\n            }\n        }\n        ret.emplace_back(make_pair(i,\
    \ e));\n        e = 0;\n    }\n    if (n!=1) ret.emplace_back(make_pair(n,1));\n\
    \    return ret;\n}"
  dependsOn: []
  isVerificationFile: false
  path: cpp/lib/prime_factorize.hpp
  requiredBy: []
  timestamp: '2020-10-18 00:00:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - cpp/test/prime_factorize.test.cpp
documentation_of: cpp/lib/prime_factorize.hpp
layout: document
redirect_from:
- /library/cpp/lib/prime_factorize.hpp
- /library/cpp/lib/prime_factorize.hpp.html
title: cpp/lib/prime_factorize.hpp
---
