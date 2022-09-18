from collections import deque
from src.core.graph import expand_node, get_node_number
from src.core.print_maze import get_maze_step, print_maze
from src.core.utils import find_node

def depth_search(maze):
    print(maze)
