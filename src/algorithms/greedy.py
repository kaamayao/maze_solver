'''
    Todos los nodos de la grafica son numerados de esta forma:

    |1|2|3| 
    |4|5|6| 
    |7|8|9| 

    el valor del nodo es guardado como NodeNumber
'''

from collections import deque

from src.core.graph import expand_node, get_node_number, get_node_coordinates

from src.core.print_maze import get_maze_step, print_maze

from src.core.tree import Tree_maze

from src.core.utils import find_node
import math


def greedy_search(maze):


    export_tree = len(maze) <= 6
    
    index_maze_step = 1
   
    cur_node = 1
    
    if export_tree:
        
        Tree_maze.add_root(1)

    objective_node = get_node_number(maze,len(maze)  - 1 ,len(maze[0])-2)
    
    cordinates_objetive = get_node_coordinates(maze,objective_node)
    
    frontier = deque([cur_node])
    reached = [cur_node]

    if(cur_node == objective_node): 
        return cur_node
    
    while frontier:
        
        cur_node = frontier.pop()
        children = expand_node(maze, cur_node) #[2,3,4]
        
        if(len(children)>0):
            
            child_values = {}
            for child in children:
                
                cordenada = get_node_coordinates(maze,child) #calcula la coordenada
                value = sum(list(map(lambda x,y: abs(x-y) , cordenada, cordinates_objetive))) #calcula la distancia manhattan
                child_values[child] = value # agrega al diccionario los hijos con sus respectivas distancias Manhattan
                
                if export_tree:
                    Tree_maze.add_node(child, cur_node)

                if(child == objective_node):
                   
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
                    return child 
                
                if not find_node(reached, child): 
                    reached.append(child)
                    frontier.append(child)
                    
                
            next_node = min(child_values, key=child_values.get) #encuentro el nodo con distancia manhattan mas chiki
            
            if next_node in frontier:
                frontier.remove(next_node) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
                frontier.append(next_node)
        
        print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
        # Incrementar el indice usado para imprimir archivos en maze(i).png
        index_maze_step+=1
    # En caso de no encontrar el nodo objetivo sobreescribir el archivo tree.tx 
    # si y solo export_tree es True
    Tree_maze.clear_generated_tree(export_tree)

