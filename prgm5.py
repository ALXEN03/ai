import heapq

g = {
    'A':{'B':2,'C':5},
    'B':{'D':4,'E':2},
    'C':{'H':2},
    'D':{'G':3},
    'E':{'G':2,'H':3},
    'H':{'G':1},
    'G':{}
}

h = {
    'A':6,
    'B':4,
    'C':4,
    'D':3,
    'E':2,
    'H':1,
    'G':0
}

q=[(h['A'],0,'A',['A'])]

while q:
    f,c,v,p=heapq.heappop(q)

    if v=='G':
        print("Path :",p)
        print("Cost :",c)
        break

    for x,w in g[v].items():
        heapq.heappush(q,(c+w+h[x],c+w,x,p+[x]))
