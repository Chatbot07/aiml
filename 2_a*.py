def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node) #  E G C
        closed_set = set()#A B
        g = {} #store distance from starting node
        parents = {}# parents contains an adjacency map of all nodes
 
        #ditance of starting node from itself is zero
        g[start_node] = 0
        #start_node is root node i.e it has no parent nodes
        #so start_node is set to its own parent node
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:#3>
            n = None#A
 
            #node with lowest f() is found
            for v in open_set:#B,E
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v#B
                    #2+6=>8<0+11=>11
             
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):#B (C,1),(G,9)
                    #nodes 'm' not in first and last set are added to first
                    #n is set its parent
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)#C,G
                        parents[m] = n#B-->A,E-->A,c-->B,g-->B,d-->E,g-->D
                        g[m] = g[n] + weight#0+2=>2,0+3=>3,2+1=3
                        print(1,g[m])
                        print(1,parents[m])
                        print(1,m,n)
                         
     
                    #for each node m,compare its distance from start i.e g(m) to the
                    #from start through n node
                    else:
                        if g[m] > g[n] + weight:
                            #update g(m)
                            print(2,g[m])
                            g[m] = g[n] + weight
                            print(2,m,n)
                            #change parent of m to n
                            parents[m] = n
                            print(2,parents[m])
                             
                            #if m in closed set,remove and add to open
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:#B-->A,E-->A,c-->B,g-->B,d-->E,g-->D
                path = []
 
                while parents[n] != n:#A!=A
                    path.append(n)#G,D,E,A
                    n = parents[n]#A
 
                path.append(start_node)
 
                path.reverse()#A,E,D,G
 
                print('Path found: {}'.format(path))
                return path
 
 
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None
         
#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):#A
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes
def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
             
        }
 
        return H_dist[n]
 
#Describe your graph here  
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
aStarAlgo('A', 'G')
