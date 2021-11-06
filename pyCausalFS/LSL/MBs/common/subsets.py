from itertools import combinations


def subsets(nbrs, k):
    return set(combinations(nbrs, k))

