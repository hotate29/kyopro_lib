# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize


from python.lib.prime_factrize import prime_factorize as pf


q = int(input())
for _ in range(q):
  ai = int(input())
  r = pf(ai)
  out = ""
  for pi,ei in r:
    out += (str(pi)+" ")*ei
  print(len(r),out)
