#Graph Coloring Problem
colors=['Red','Blue','Green']
states=['a','b','c','d']
neighbors={}
neighbors['a']=['b','c','d']
neighbors['b']=['a','d']
neighbors['c']=['a','d']
neighbors['d']=['c','b','a']

colors_of_states={}

def promising(state,color):#d,green
    for neighbor in neighbors.get(state):#c,b,a
        color_of_neighbor=colors_of_states.get(neighbor)#blue
        if color_of_neighbor==color:#b==b
            return False
    return True

def get_color_for_state(state):#d
    for color in colors:#Red,Blue,Green
        if promising(state,color):#d,Red
            return color

def main():
    for state in states:#c,d
        colors_of_states[state]=get_color_for_state(state)#a:Red,b:blue,c:blue,d:green

    print(colors_of_states)

main() 
