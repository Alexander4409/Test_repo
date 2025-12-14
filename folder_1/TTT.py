# Улучшенный вариант — несколько рандомных запусков + degree-based эвристика
# Вход: N M, затем M строк u v (0-based). Вывод: K, затем K индексов удалённых рёбер (0-based).
import sys, random, collections
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)
it = iter(data)
N = next(it); M = next(it)
edges = []
adj = [[] for _ in range(N)]
for idx in range(M):
    u = next(it); v = next(it)
    edges.append((u, v))
    adj[u].append((v, idx))
    adj[v].append((u, idx))

# вычислим степени (учитываем кратные рёбра; петли будут давать +2 для одинаковых концов)
deg = [len(adj[v]) for v in range(N)]

# функция: построить остов деревом (N-1 рёбер) методом итеративного DFS,
# где порядок соседей для каждого узла формируется рандомизированно + сортировка по степени соседа
def build_tree_random():
    visited = [False]*N
    order = [None]*N
    # подготовим порядок обхода для каждой вершины: перемешаем, затем сортируем по deg (для тенденции углубляться)
    for v in range(N):
        lst = adj[v][:]
        random.shuffle(lst)
        lst.sort(key=lambda x: deg[x[0]])
        order[v] = lst

    iter_idx = [0]*N
    stack = []
    tree_edge_ids = []

    visited[0] = True
    stack.append(0)
    while stack:
        v = stack[-1]
        # пропускаем уже посещённых соседей
        while iter_idx[v] < len(order[v]) and visited[order[v][iter_idx[v]][0]]:
            iter_idx[v] += 1
        if iter_idx[v] < len(order[v]):
            nei, eidx = order[v][iter_idx[v]]
            iter_idx[v] += 1
            if not visited[nei]:
                visited[nei] = True
                tree_edge_ids.append(eidx)
                stack.append(nei)
        else:
            stack.pop()

    # На всякий случай (если граф не был связным — по условию он связный),
    # присоединим остальные компоненты (гарантируем N-1 рёбер)
    if sum(visited) != N:
        for s in range(N):
            if not visited[s]:
                visited[s] = True
                stack = [s]
                while stack:
                    v = stack.pop()
                    for nei, eidx in adj[v]:
                        if not visited[nei]:
                            visited[nei] = True
                            tree_edge_ids.append(eidx)
                            stack.append(nei)
    # tree_edge_ids может содержать более N-1 рёбер в редких случаях (если добавляли в запасных обходах) — обрежем:
    if len(tree_edge_ids) > N-1:
        tree_edge_ids = tree_edge_ids[:(N-1)]
    return tree_edge_ids

# функция: посчитать "score" (KPI) как сумму расстояний от 0 по дереву, построенному по списку рёбер
def score_tree(tree_edge_ids):
    tree_adj = [[] for _ in range(N)]
    for eidx in tree_edge_ids:
        u,v = edges[eidx]
        tree_adj[u].append(v)
        tree_adj[v].append(u)
    # BFS
    from collections import deque
    dist = [-1]*N
    dq = deque([0])
    dist[0] = 0
    while dq:
        x = dq.popleft()
        for y in tree_adj[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                dq.append(y)
    # если какой-то узел недостижим — считаем очень плохой вариант
    if any(d == -1 for d in dist):
        return -10**18
    return sum(dist)  # цель — максимизировать

# основной цикл: несколько попыток, сохраняем лучший остов
best_tree = None
best_score = -10**18
ATTEMPTS = 20  # у вас 20 попыток — используем все
# небольшая оптимизация: если M == N-1, уже дерево — ничего удалять
if M == N-1:
    best_tree = list(range(M))
    best_score = score_tree(best_tree)
else:
    for _ in range(ATTEMPTS):
        t = build_tree_random()
        if len(t) < N-1:
            # мало рёбер — плохой вариант, пропускаем
            continue
        sc = score_tree(t)
        if sc > best_score:
            best_score = sc
            best_tree = t[:]

# Если всё же не нашлось корректного остова (маловероятно) — fallback: простая BFS-остов
if best_tree is None:
    visited = [False]*N
    parent_edge = [-1]*N
    from collections import deque
    dq = deque([0]); visited[0]=True
    while dq:
        v = dq.popleft()
        for nei,eidx in adj[v]:
            if not visited[nei]:
                visited[nei]=True
                parent_edge[nei]=eidx
                dq.append(nei)
    tree_ids = [e for e in parent_edge if e!=-1]
    best_tree = tree_ids[:N-1]

tree_set = set(best_tree)
removed = [i for i in range(M) if i not in tree_set]
K = len(removed)
# вывод
out = []
out.append(str(K))
if K>0:
    out.append(" ".join(map(str, removed)))
else:
    out.append("")
sys.stdout.write("\n".join(out))
