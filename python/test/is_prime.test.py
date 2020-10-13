# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C


from python.lib.is_prime import isprime


print(sum(isprime(int(input())) for _ in range(int(input()))))
