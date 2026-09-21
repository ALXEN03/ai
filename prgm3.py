import heapq

g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['G'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}

h = {
    'A':5,
    'B':3,
    'C':2,
    'D':6,
    'E':1,
    'F':0,
    'G':4
}

def best(s,goal):
    q=[(h[s],s)]
    vis=set()

    while q:
        _,v=heapq.heappop(q)
        print(v,end=' ')

        if v==goal:
            print('\nGoal reached!')
            return

        if v not in vis:
            vis.add(v)
            for x in g[v]:
                heapq.heappush(q,(h[x],x))

best('A','F')
