from collections import deque
from src.core.graph import expand_node, get_node_number
from src.core.print_maze import get_maze_step, print_maze
from src.core.tree import Tree_maze
from src.core.utils import find_node

def depth_search(maze):
    export_tree = len(maze) <= 6
    index_maze_step = 1
    step = 1
    cur_node = 1
    if export_tree:
        Tree_maze.add_root(1)
    objective_node = get_node_number(maze,len(maze) - 1 ,len(maze[0])-2)
    frontier = deque([cur_node])
    reached = [cur_node]
    if(cur_node == objective_node): 
        return cur_node
    while frontier:
        cur_node = frontier.pop()
        children = expand_node(maze, cur_node)
        if(len(children)>0):
            for child in children: 
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
        print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
        index_maze_step+=1
    Tree_maze.clear_generated_tree(export_tree)
