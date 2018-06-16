from collections import defaultdict
edges = []
cnt = 0
config=input().split()
for j in range(int(config[1])):
    i = input().split()
    edges.append((i[0],i[1]))
adj_list = defaultdict(list)
print(edges)
for start, end in edges:
    adj_list[end].append(start)
print(adj_list)
def dfs_iter(graph, root):
    visited = []
    stack = [root, ]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([x for x in graph[node] if x not in visited])
            print(stack)
    print(visited)
    return visited
b=[]
for a in adj_list:
    b.append(a)
for a in b:
    if int(a)==6:
        if len(dfs_iter(adj_list, a)) % 2 == 0:
            cnt += 1
print (cnt)