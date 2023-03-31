def neg_ls(ls, n, m):
    return [(-x) if 3 <= x <= 8 else x for x in ls]

print(neg_ls([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 8))