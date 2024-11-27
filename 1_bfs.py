 graph={
    '5':['2','3'],
    '2':['4','8'],
    '3':['6'],
    '4':[],
    '8':['7'],
    '6':[],
    '7':[]
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    queue.append(node)
    visited.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS Nodes are:")
bfs(visited,graph,'5')
