def isprime(n: int) -> bool:
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, n + 1,2):
        if i * i <= n:
            if n % i == 0:
                return False
        else:
            break
    return True


if __name__ == "__main__":
    for i in range(100):
        print(i, isprime(i))
