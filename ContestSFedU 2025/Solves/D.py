def search(start, dest, city, visited=set()):
    to_visit = set(city[start]) - visited
    for curr in to_visit:
        if curr == dest:
            return city[start][curr]

        if (cost := search(curr, dest, city, visited | {start})):
            return max(cost, city[start][curr])
    return None


city = {}
n, m = map(int, input().split())
for i in range(n - 1):
    u, v, c = map(int, input().split())
    try:
        city[u][v] = c
    except KeyError:
        city[u] = {v: c}
    try:
        city[v][u] = c
    except KeyError:
        city[v] = {u: c}

a = list(map(int, input().split()))

cache = {}
total_cost = 0
for i in range(len(a) - 1):
    start, end = a[i], a[i + 1]
    cost = cache.get(start, {}).get(end, search(start, end, city))
    try:
        cache[start][end] = cost
    except KeyError:
        cache[start] = {end: cost}
    try:
        cache[end][start] = cost
    except KeyError:
        cache[end] = {start: cost}

    total_cost += cost
print(total_cost)
