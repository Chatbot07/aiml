#Travelling Salesman Problem
from sys import maxsize
from itertools import permutations
v=4
def travellingSalesmanProblem(graph,s):
    vertex=[]#[1,2,3]
    for i in range(v):#(0,4)0,1,2,3
        if i!=s:#1!=0
            vertex.append(i)#1 2 3
    min_path=maxsize
    next_permutation=permutations(vertex)#[1,2,3][1,3,2][2,1,3][2,3,1]
                                         #[3,1,2][3,2,1]
    for i in next_permutation:#[1,2,3][1,3,2][2,1,3][2,3,1]
                                         #[3,1,2][3,2,1]
        current_pathweight=0
        k=s#00][
        for j in i:#[1,2,3] #3
            current_pathweight+=graph[k][j]#75
            k=j#3
        current_pathweight+=graph[k][s]#75+20=95
        min_path=min(min_path,current_pathweight)#95
    return min_path#80

graph=[[0,10,15,20],[10,0,35,25],
           [15,35,0,30],[20,25,30,0]]
s=0
print(travellingSalesmanProblem(graph,s))#80
