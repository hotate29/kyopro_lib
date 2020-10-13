# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A


from python.lib.prime_factorize import prime_factorize as pf


if __name__ == "__main__":
    n = int(input())
    r = prime_factorize(n)
    ans = []
    for p, e in r:
        p = str(p)
        for i in range(e):
            ans.append(p)
    print(f"{n}:", " ".join(ans))
