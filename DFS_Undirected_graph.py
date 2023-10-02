from collections import defaultdict
def dfs(graphs,start,path,visited):
    visited[start]=True
    path.append(start)
    for neighbour in graphs[start]:
        if visited[neighbour]==False:
            dfs(graphs,neighbour,path,visited)
    return path   
graphs=defaultdict(list)
v,e=map(int,input().split())
for i in range(e):
    u,v=map(str,input().split())
    graphs[u].append(v)
    graphs[v].append(u)
for v in graphs:
    print(v,graphs[v])
path=[]
visited=defaultdict(bool)
start='A'
dfs_path=dfs(graphs,start,path,visited)
print(dfs_path)
    