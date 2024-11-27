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
stack=[]
def dfs(visited,graph,node):
    if node not in visited:
        visited.append(node)
        stack.append(node)
        
        n=stack.pop(0)#5
        print(n,end=" ")
        for neighbour in graph[node]:#2,3
            dfs(visited,graph,neighbour)

print("DFS nodes are:")
dfs(visited,graph,'5')
