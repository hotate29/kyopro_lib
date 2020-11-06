from itertools import product


def BitFullSearch(a):
    bits = [(0,1) for _ in range(len(a))]
    p = product(*bits)
    return ((ai for ai,bi in zip(a,pi) if bi) for pi in p)
