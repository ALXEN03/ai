from collections import deque

g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

def bfs(s):
    q=deque([s])
    vis=set()
    while q:
        v=q.popleft()
        if v not in vis:
            print(v,end=' ')
            vis.add(v)
            q.extend(g[v])

bfs('A')
