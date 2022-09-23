

from collections import deque
from src.core.graph import expand_node, get_node_number
from src.core.print_maze import get_maze_step, print_maze
from src.core.tree import Tree_maze
from src.core.utils import find_node

def depth_iterative_search(maze):
   
    export_tree = len(maze) <= 6
    index_maze_step = 1
    cur_node = 1
    
    
    if export_tree:    
        Tree_maze.add_root(1)
        
    objective_node = get_node_number(maze,len(maze) - 1 ,len(maze[0])-2)
    frontier = deque([cur_node])
    reached = [cur_node]
    
    if(cur_node == objective_node): 
        return cur_node
    
    jump = 3 #que tan profundo quiero que escarbe
    nodes_values = {}
    nodes_values[cur_node] = 0 #Esto me dará la altura del nodo
    hight = 0
    
    while frontier:
       
        cur_node = frontier.pop()
        children = expand_node(maze, cur_node)

        if(len(children)>0):
            for child in children:
                
                nodes_values[child] = nodes_values[cur_node] + 1 
                 
                if export_tree:
                    Tree_maze.add_node(child, cur_node)
                    
                if(child == objective_node):
                    
                    Tree_maze.clear_generated_tree(export_tree)
                    
                    reached.append(child)
                    
                    print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
                    return child 
                
                if not find_node(reached, child): 
                    reached.append(child)
                    if nodes_values[child] <= hight :
                        frontier.append(child)
                    else:
                        frontier.appendleft(child)
        
                else:
                    nodes_values.pop(child)

            nodes_values.pop(cur_node)

            #print(nodes_values)
        #print(nodes_values[min(nodes_values, key=nodes_values.get)])
        if nodes_values[min(nodes_values, key=nodes_values.get)] == hight+1 :
            hight += jump
    
        #print(hight)

        print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)

        index_maze_step+=1
        
        
    
    Tree_maze.clear_generated_tree(export_tree)
