from itertools import product


def BitFullSearch(a):
    p = product((0,1),repeat=len(a))
    return ((ai for ai,bi in zip(a,pi) if bi) for pi in p)