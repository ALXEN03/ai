g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

def dfs(v,vis):
    if v not in vis:
        print(v,end=' ')
        vis.add(v)
        for x in g[v]:
            dfs(x,vis)

dfs('A',set())
