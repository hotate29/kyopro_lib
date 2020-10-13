def isprime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n + 1):
        if i * i <= n:
            if n % i == 0:
                return False
    return True


if __name__ == "__main__":
    for i in range(100):
        print(i, isprime(i))
