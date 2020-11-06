# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A
from python.lib.Bit_Full_search import BitFullSearch
from math import ceil


n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

c = {sum(ci) for ci in BitFullSearch(a)}
for mi in m:
    if mi in c:
        print("yes")
    else:
        print("no")
