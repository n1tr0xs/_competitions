n = int(input())
strings = [input() for i in range(n)]

for s in strings:
    consonance = {}
    for t in strings:
        if s == t:
            continue

        curr = consonance.get(0, None)
        if (curr is None) or (t < curr):
            consonance[0] = t

        for k in range(1, min(len(s), len(t))):
            suff = s[-k:]
            pref = t[:k]
            curr = consonance.get(k, None)
            if suff == pref:
                if (curr is None) or (t < curr):
                    consonance[k] = t
    print(consonance[max(consonance)])
