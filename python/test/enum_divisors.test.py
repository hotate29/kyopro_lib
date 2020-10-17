# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D

from python.lib.enum_divisors import enum_divisors


a,b,c = map(int,input().split())
ans = 0
for di in enum_divisors(c):
    ans += a <= di <= b
print(ans)
