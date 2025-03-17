def mex(arr):
    _arr = set(arr)
    k = 0
    while True:
        if k not in _arr:
            return k
        k += 1


def calc_b(n, a):
    b = []
    for i in range(len(a)):
        pref = a[:i + 1]
        suf = a[i:]
        b.append(mex(pref) + mex(suf))
    return b


n = int(input())
a = list(map(int, input().split()))
print(*calc_b(n, a))
