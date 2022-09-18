from collections import deque
from src.core.graph import expand_node, get_node_number
from src.core.print_maze import get_maze_step, print_maze
from src.core.utils import find_node

def breadth_search(maze):
    index_maze_step = 1
    step = 1;
    cur_node = 2
    objective_node = get_node_number(maze,len(maze),len(maze[0])-1)
    frontier = deque([cur_node])
    reached = []
    if(cur_node == objective_node): 
        return cur_node
    while frontier:
        cur_node = frontier.pop()
        children = expand_node(maze, cur_node)
        if(len(children)>0):
            for child in children: 
                if(child == objective_node):
                    return child 
                if not find_node(reached, child): 
                    reached.append(child)
                    frontier.appendleft(child)
        print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
        index_maze_step+=1
